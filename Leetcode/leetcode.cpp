#include <limits>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <queue>

using namespace std;

#define mp make_pair
#define ll long long

vector<int> dailyTemperatures(const vector<int>& temperatures) {

    vector<int> ret(temperatures.size(), 0);
    queue<pair<int, int>> q;
    q.push(mp(0, temperatures[0]));
    for(int i{1}; i < temperatures.size(); i++){
        
        if(q.empty()) q.push(mp(i, temperatures[i]));

        while(!q.empty() && q.front().second < temperatures[i]){
            ret[q.front().first] = i - q.front().first;
            q.pop();
        }

        q.push(mp(i, temperatures[i]));
    }

    while(!q.empty()){
        ret[q.front().first] = 0;
        q.pop();
    }

    return ret;
}

int main()
{
    vector<int> test = {73,74,75,71,69,72,76,73};
    vector<int> res;
    res = dailyTemperatures(test);

    return 0;
}