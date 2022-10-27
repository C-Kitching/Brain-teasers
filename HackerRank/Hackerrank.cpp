#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */  
    
    std::string S{""};
    std::vector<std::string> history;
    std::string operation;
    std::string W;
    int to_delete;
    int index;
    
    int Q;
    std::cin >> Q;
    for(int i{0}; i < Q; i++){
        std::cin >> operation;
        
        if(operation == "1"){
            history.push_back(S);
            std::cin >> W;
            S += W;
        }
        else if(operation == "2"){
            history.push_back(S);
            std::cin >> to_delete;
            S.erase(S.size() - to_delete, to_delete);
        }
        else if(operation == "3"){
            std::cin >> index;
            std::cout << S[index - 1] << "\n";
        }
        else{
            S = history.back();
            history.pop_back();
        }
    }
        
    return 0;
    }