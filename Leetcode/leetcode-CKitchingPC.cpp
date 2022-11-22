
#include <cctype>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
using namespace std;

int romanToInt(string s) {
        
    // maps numerals to values
    unordered_map<string, int> value_map{{"I", 1}, {"V", 5}, {"X", 10}, {"L", 50}, 
                                    {"C", 100}, {"D", 500}, {"M", 1000}};
    
    // maps numerals to other numerals that they modify
    // for example: 'C' modifys the values of 'D' and 'M'
    unordered_map<string, unordered_set<string>> modifier_map;
    modifier_map["C"] = {"D", "M"};
    modifier_map["X"] = {"L", "C"};
    modifier_map["I"] = {"V", "X"};
    
    int N = s.size();
    
    // one roman numeral
    if(N == 1) return value_map[s];
    
    // loop over remaining numerals
    int res{0};
    string potential_modifier{s[0]};
    string curr_char;
    for(int i{1}; i < N; i++){
        curr_char = s[i];
        
        // if previous numeral modifies the current one
        unordered_set<string> modified_numerals = modifier_map[potential_modifier];
        if(modified_numerals.find(curr_char) != modified_numerals.end()){
            res += value_map[curr_char] - value_map[potential_modifier];

            // set potential modifier to the next numeral and then skip
            // one numeral
            potential_modifier = s[i+1];
            i++;

            // if we're on the last numeral, add it's value too
            if(i == N-1) res += value_map[potential_modifier];
        }
        
        // if previous doesn't modifiy then append its value
        else{
            res += value_map[potential_modifier];
            potential_modifier = curr_char;

            // if we're on the last numeral, add it's value too
            if(i == N-1) res += value_map[potential_modifier];
        }
    }
    
    return res;
    
}

int main(){

    int num = romanToInt("MCMXCIV");
    cout << num;

    return 0;
}