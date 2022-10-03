# Coding problems

A collection of interesting problems solved with programming.

## Problems

1. **The red and blue hat problem**  
One hundred prisoners are lined up single file. A blue or red hat is placed on each of their heads randomly. The prisoners cannot see the color of the hat on their own head, but they can see the colors of all the hats in front of them. The prisoner in the back can clearly see all 99 hats in front of him. The 50th prisoner in line can see the 49 hats in front of him, and the prisoner in the front of the line cannot see anything but the forest before him. Also, the prisoners don't know the proportion of red hats to blue hats in advance—it could be 50/50, but it could also be any combination that adds to 100.  
A guard is going to walk down the line, starting in the back, and ask each prisoner what color hat they have on. They can only answer "blue" or "red." If they answer incorrectly, or say anything else, they will be shot dead on the spot. If they answer correctly, they will be set free. Each prisoner can hear all of the other prisoners' responses, as well as any gunshots that indicate an incorrect response. They can remember all of this information.  
Before the executions begin, the prisoners get to huddle up and make a plan. How can the prisoners ensure that the most people possible survive?  

2. **Missing integers**   
Suppose we have 98 distinct integers from I to I 00. What is a good way to find out the two missing integers (within [ 1, 100])?

3. **Tortoise and the hare - cycle detection algorithms**  
Cycle detection is the algorithmic problem of finding a cycle in a sequence of iterated function values.  
For any function $f$ that maps a finite set $S$ to itself, and any initial value $x_{0}$ in $S$, the seqeunce of iterated function values
$$x_{0}, x_{1} = f(x_{0}), x_{2}=f(x_{1}),...,x_{i}=f(x_{i-1}), ...$$
must eventually use the same value twice: there must be some pair of distinct indicies $i$ and $j$ such that $x_{i} = x_{j}$. Once this happens, the sequence must continue periodically, by repeating the same sequence of values from $x_{i}$ to $x_{j-1}$. Cycle deterction is the problem of finding $i$ and $j$ given $f$ and $x_{0}$.   
To do this, we can use Floyd's tortoise and hare algorithm [1].  

4. **Blackjack**  
Given two blackjack hands can we determine which one would win?  
For example (K,Q) would beat (2,3).  
The complication with this problem involves determining the optimal representation for the A's, as these can be high or low.  

5. **Sum of odd length subarrays**  
Given an array, determine the sum of all odd length subarrays.  
For example: [2,4,7]  
The possible subarrays are: [2], [4], [7], [2,4], [4,7], [2,4,7]  
The total sum of those subarrays is = 2 + 4 + 7 + 6 + 11 + 13 = 43  
This problem can be solved by brute-force in $O(n^{3})$ time, however there exists an order $O(n)$ solution.  
Consider how many times the element $A[k]$ appears in the sum.  
There are exactly $(i+1)$ subarrays ending in $A[k]$, and exactly $(n-i)$ subarrays starting with $A[k]$, therefore the total amound of subarrays of any length containing $A[k]$ is $k = (i+1)(n-i)$ where $n$ is the length of the original array.  
Of those subarrays, $(k+1)/2$ are of odd length.  
Therefore we simply need to loop through the array one time and iterate the sum 
$$S_{i} = A[k] * \frac{(i+1)(n-i)+1}{2}$$.


## Referecnes
1 - https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare
