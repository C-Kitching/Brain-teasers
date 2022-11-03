// Title: Google Kick Start
// Name: Christopher Robert Kitching
// E-mail: christopher.kitching@manchester.ac.uk
// Date created: 17/10/22
// Last editied: 17/10/22
// Description: File to test Leetcode solutions

#include <vector>
#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
    // parse both lists
    int val1 = l1->val;
    while(l1 != NULL){
        l1 = l1->next;
        val1 *= 10;
        val1 += l1->val;
    }
    cout << val1;

    
    return l2;
    
    
    
    
}
    


int main()
{
    ListNode* l1;
    ListNode* l2;

    addTwoNumbers(l1, l2);


    return 0;
}