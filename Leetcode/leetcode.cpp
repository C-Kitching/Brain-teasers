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
<<<<<<< HEAD

using namespace std;

int coinChange(vector<int>& coins, int n) {
        
    // initalise variables
    int* dp = new int[n+1];
    
    dp[0] = 0; // 0 coins needed to make 0 total
    
    // sort array
    sort(coins.begin(), coins.end());
    
    // determine how to make each possible value
    // using the minimum number of coins
    for(int i{1}; i<=n; i++){
        
        dp[i] = INT_MAX;
        
        for(auto c : coins){
            
            // if the value of the coin is greater than the value we are trying to make
            // then move to making next value in the list
            if(i - c < 0) break;
            
            // best way to make current amount
            // is the min 
            if(dp[i-c] != INT_MAX) dp[i] = min(dp[i], 1 + dp[i-c]);

        }
    }
    
    return dp[n] == INT_MAX ? -1 : dp[n];
    
}
    


int main()
{
    vector<int> coins;
    coins.push_back(1);
    coins.push_back(2);
    coins.push_back(5);
    int n{11};

    int change = coinChange(coins, n);
    cout << change;
=======
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


>>>>>>> 93889f7e6373b65265270926f4333466ee2ff2be

    return 0;
}