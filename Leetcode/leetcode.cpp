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

bool wordBreak(string s, unordered_set<string> &dict) {
    if(dict.size()==0) return false;
    
    vector<bool> dp(s.size()+1,false);
    dp[0]=true;
    
    for(int i=1;i<=s.size();i++)
    {
        for(int j=i-1;j>=0;j--)
        {
            if(dp[j])
            {
                string word = s.substr(j,i-j);
                if(dict.find(word)!= dict.end())
                {
                    dp[i]=true;
                    break; //next i
                }
            }
        }
    }
    
    return dp[s.size()];
}

int main()
{
    string haystack = "leetcode";
    unordered_set<string> set = {"leet", "code"};
    cout << wordBreak(haystack, set); 

    return 0;
}