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

bool possibleBipartition(int n, vector<vector<int>>& dislikes) {
        
    // create adjacency list and colour map
    unordered_map<int, unordered_set<int>> A;
    unordered_map<int, int> colours; 
    for(auto& edge : dislikes){
        A[edge[0]].insert(edge[1]);
        A[edge[1]].insert(edge[0]);
        if(colours.find(edge[0]) == colours.end()) colours[edge[0]] = WHITE;
        if(colours.find(edge[1]) == colours.end()) colours[edge[1]] = WHITE;
    }

    // start bfs from each node
    for(int i{1}; i <= n; i++){
        
        // push initial node to queue
        queue<int> q;
        q.push(i);

        // bsf
        while(!q.empty()){

            // get next node
            int node = q.front();
            q.pop();

            // first time at node
            if(colours[i] == WHITE) colours[i] = RED;

            // set all neighbours to opposite colour
            for(auto& neighbour : A[i]){

                // found an invalid connection
                if(colours[i] == colours[neighbour]) return false;

                // else set colour of neighbour opposite to current node
                if(colours[neighbour] == WHITE){
                    colours[i] == RED ? colours[neighbour] = BLUE : colours[neighbour] = RED;

                    // add neighbour to queue
                    q.push(neighbour);
                }
            }
        }
    }

    return true;
}

int main()
{
    vector<vector<int>> test = {{1,2},{1,3},{2,4}};
    bool b = possibleBipartition(4, test);

    cout << b << endl;

    return 0;
}