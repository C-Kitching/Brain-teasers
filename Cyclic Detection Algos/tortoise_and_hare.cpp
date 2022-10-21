// Title: Tortoise and hare
// Name: Christopher Robert Kitching
// E-mail: christopher.kitching@manchester.ac.uk
// Date created: 24/09/22
// Last editied: 25/09/22
// Description: Implementation of tortoise and hare algorithm to find the
//              number of unique elements in a cycling array

// includes
#include <iostream>
#include <math.h>

// preprocessor directive for recurrance function
#define f(X, P, Q) (X*P + Q)

// create alias for long long
typedef unsigned long long ulong;

// hare and tortoise algorithm to find cycle length
int hare_and_tortoise(const int N, const int& S, 
                      const int& P, const int& Q, 
                      const ulong& k){
    
    // initial position
    ulong x_0{S%k};
    ulong count{1};

    // initalise hare and tortoise positions
    ulong tortoise = f(x_0, P, Q)%k;
    ulong hare = f(f(x_0, P, Q)%k, P, Q)%k;
    
    // find repetition in sequence
    while(tortoise != hare){

        // if tortoisue reached end of array without finding loop
        // all elements are unique so return length of array
        if(count >= N) return count;
        else count++;

        // update tortoise and hare position
        tortoise = f(tortoise, P, Q)%k;
        hare = f(f(hare, P, Q)%k, P, Q)%k;
    }
    
    // find position of the first repetition
    ulong mu{0};
    tortoise = x_0;
    while(tortoise != hare){
        tortoise = f(tortoise, P, Q)%k;
        hare = f(hare, P, Q)%k;
        mu++;
    }
    
    // Find the length of the shortest cycle starting from x_mu
    // The hare moves one step at a time while tortoise is still.
    // lam is incremented until lam is found.
    ulong lam{1};
    hare = f(tortoise, P, Q)%k;
    while(tortoise != hare){
        hare = f(hare, P, Q)%k;
        lam++;
    }
    
    return lam + mu;
}

int main() {  
    
    // declare variables
    int N, S, P, Q;
    
    // read in data
    N = 100000000;
    S = 569099406;
    P = 1607140150;
    Q = 823906344;

    // cast modulo to long long
    ulong k = static_cast<ulong>(std::pow(2, 31));
    
    // solve
    std::cout << hare_and_tortoise(N, S, P, Q, k);
    
    return 0;
}