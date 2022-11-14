// Title: Google Kick Start
// Name: Christopher Robert Kitching
// E-mail: christopher.kitching@manchester.ac.uk
// Date created: 17/10/22
// Last editied: 17/10/22
// Description: File to test Leetcode solutions

#include <vector>
#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <set>

using namespace std;

int countDistinctIntegers(vector<int>& nums) {
        
    vector<int> temp;
    for(int j{0}; j < nums.size(); j++){
        string s = to_string(nums[j]);
        reverse(s.begin(), s.end());
        temp.push_back(stoi(s));
    }        

    vector<int> new_nums;
    new_nums.reserve(nums.size() + temp.size()); // preallocate memory
    new_nums.insert(new_nums.end(), nums.begin(), nums.end() );
    new_nums.insert(new_nums.end(), temp.begin(), temp.end() );
    
    // convert to set and then back to vector
    set<int> set;
    for(int i{0}; i < new_nums.size(); i++) set.insert(new_nums[i]);
    new_nums.assign(set.begin(), set.end());
    
    return new_nums.size();
}

int main()
{
    vector<int> v{1,13,10,12,31};
    int x = countDistinctIntegers(v);
    cout << x;



    return 0;
}