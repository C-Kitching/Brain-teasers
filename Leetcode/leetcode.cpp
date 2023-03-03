#include <limits>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define mp make_pair
#define WHITE 0
#define RED 1
#define BLUE 2
#define ll long long

int strStr(string haystack, string needle) {
    int i{0}, j{0};
    while(i < haystack.size()){
        int res{i};
        while(haystack[i] == needle[j] && j < needle.size() && i < haystack.size()){
            i++; j++;
        }
        if(j == needle.size()) return res;
        else{
            i = res + 1;
            j = 0;
        }
    }
    return -1;
}

int main()
{
    string haystack = "leetcode";
    string needle = "leeto";
    cout << strStr(haystack, needle); 

    return 0;
}