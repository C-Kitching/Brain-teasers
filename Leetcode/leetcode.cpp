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

int maxProfit(vector<int>& prices) {
        
    int N = prices.size();
    int profit{0};
    int buy_price;

    for(int i{0}; i < N - 1; i++){

        // find valley and buy
        while(prices[i+1] <= prices[i] && i < N-1) i++;
        buy_price = prices[i];

        // find peak and sell
        while(prices[i+1] > prices[i] && i < N-1) i++;
        profit += prices[i] - buy_price;

    }

    return profit;


}

int main()
{
    vector<int> v{1,2};
    int x = maxProfit(v);
    cout << x;



    return 0;
}