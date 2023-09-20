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

vector<int> spiralOrder(vector<vector<int>>& matrix) {
        
    int m = matrix.size();
    int n = matrix[0].size();
    vector<int> res(m*n);
    int i{0};
    int l{0}, r{n-1}, u{0}, d{m-1};

    while(l <= r && u <= d){

        // add top layer
        for(int col{l}; col <= r; col++) res[i++] = matrix[u][col];
        if(++u > d) break;

        // add right layer
        for(int row{u}; row <= d; row++) res[i++] = matrix[row][r];
        if(--r < l) break;

        // add bottom layer
        for(int col{r}; col >= l; col--) res[i++] = matrix[d][col];
        if(--d < u) break;

        // add left layer
        for(int row{d}; row >= u; row--) res[i++] = matrix[row][l];
        if(++l > r) break;
    }

    return res;

}

// main function
int main()
{
    vector<vector<int>> v = {{1,2,3},{4,5,6},{7,8,9}};
    spiralOrder(v);

    return 0;
}