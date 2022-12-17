#include <limits>
#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <set>

using namespace std;

#define ll long long

set<string> op = {"+", "-", "*", "/"};

ll evalRPN(vector<string>& tokens){
    string t = tokens.back();
    tokens.pop_back();
    if(t != "+" && t != "-" && t != "*" && t != "/") return stoll(t);
    else{
        ll b = evalRPN(tokens);
        ll a = evalRPN(tokens);
        if(t == "+") return a+b;
        else if(t == "-") return a-b;
        else if(t == "*") return a*b;
        else return a/b;
    }
}

int main()
{
    vector<string> test = {"2","1","+","3","*"};
    ll res;
    res = evalRPN(test);
    cout << res << endl;

    return 0;
}