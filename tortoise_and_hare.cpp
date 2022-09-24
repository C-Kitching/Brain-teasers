#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set> 
#include <math.h>
using namespace std;

// update position function
long long f(const long long& pos, const long long& S, const long long& P, 
            const long long& Q){
    return (pos*P + Q);
}

// hare and tortoise algorithm to find cycle length
int hare_and_tortoise(const long long N, const long long& S, 
                      const long long& P, const long long& Q){
    
    // initalise hare and tortoise positions
    long long tortoise{f(S, S, P, Q)}, hare{f(f(S, S, P, Q), S, P, Q)};
    
    // find repetition in sequence
    while(tortoise != hare){
        tortoise = f(tortoise, S, P, Q);
        hare = f(f(hare, S, P, Q), S, P, Q);
    }
    
    // find position of the first repetition
    int mu{0};
    tortoise = S;
    while(tortoise != hare){
        tortoise = f(tortoise, S, P, Q);
        hare = f(hare, S, P, Q);
        mu += 1;
    }
    
    // Find the length of the shortest cycle starting from x_mu
    // The hare moves one step at a time while tortoise is still.
    // lam is incremented until lam is found.
    int lam{1};
    hare = f(tortoise, S, P, Q);
    while(tortoise != hare){
        hare = f(hare, S, P, Q);
        lam += 1;
    }
    
    return lam;
}

int main() {  
    
    // declare variables
    long long N, S, P, Q, k;
    k = pow(2, 31);
    
    // read in data
    N = 3;
    S = 1;
    P = 1;
    Q = 1;
    
    // solve
    std::cout << hare_and_tortoise(N, S, P, Q);
    
    return 0;
}