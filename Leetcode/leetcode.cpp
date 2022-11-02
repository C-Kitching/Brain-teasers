// Title: Google Kick Start
// Name: Christopher Robert Kitching
// E-mail: christopher.kitching@manchester.ac.uk
// Date created: 17/10/22
// Last editied: 17/10/22
// Description: File to test Leetcode solutions

#include <vector>
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int lengthOfLongestSubstring(const string& s) {
        
    int max_length{0};
    
    // check all chars
    for(int i{0}; i < s.size(); i++){
        
        unordered_set<char> prev;
        int length{0};
        
        for(int j{i}; j < s.size(); j++){
            
            // if char not seen before
            if(prev.find(s[j]) == prev.end()){
                prev.insert(s[j]);
                length++;
            }
            
            // if seen before, move to the next char
            else break;
        }
        
        // if current length is max
        if(length > max_length) max_length = length;
        
    }
    
    return max_length;

}

int main()
{
    std::cout << lengthOfLongestSubstring("abcabcbb");


    return 0;
}