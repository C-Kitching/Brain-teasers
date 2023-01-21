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

vector<vector<int>> generate(int numRows) {
    vector<vector<int>> ret;
    for(int i{0}; i < numRows; i++){
        vector<int> row(i + 1, 1);
        for(int j{0}; j < row.size(); j++){
            if(j != 0 && j != row.size() - 1){
                row[j] = ret[i-1][j] + ret[i-1][j+1];
            }
        }
        ret.push_back(row);
    }
    return ret; 
}

int main()
{
    int r = 5;
    vector<vector<int>> x = generate(r);

    return 0;
}