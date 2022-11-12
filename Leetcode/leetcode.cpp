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

using namespace std;

// tree node structure
struct TreeNode {
    int val;
    int cost;
    int bob_visit;
    TreeNode *left;
    TreeNode *right;
    TreeNode *parent;
    TreeNode() : val(0), cost(0), bob_visit(-1), left(nullptr), right(nullptr), parent(nullptr) {}
    TreeNode(int x) : val(x), cost(0), bob_visit(-1), left(nullptr), right(nullptr), parent(nullptr) {}
    TreeNode(int x, int amount, int bob_visit, TreeNode *left, TreeNode *right, TreeNode* parent) : 
        val(x), cost(cost), bob_visit(bob_visit), left(left), right(right), parent(parent) {}
};

// build tree
TreeNode* createTree(const vector<vector<int>>& edges, int& bob, 
    const vector<int>& amount){

    //to check if node alredy exist
    unordered_map<int, TreeNode*> getNode;  

    //to check if node has parent or not                        
    unordered_map<int, bool> isChild; 

    // go through all edges
    for(auto& edge: edges){

        // if node doesn't exist in tree
        if(getNode.count(edge[0])==0){
            TreeNode* par = new TreeNode(edge[0]);  // create new node
            getNode[edge[0]] = par; // track it
        }

        // if child doesn't exist in tree
        if(getNode.count(edge[1])==0){
            TreeNode* child = new TreeNode(edge[1]);  // create child
            getNode[edge[1]] = child;  // track it
        }

        // if node already has left child, new child is right
        if(getNode[edge[0]]->left){
            getNode[edge[0]]->right = getNode[edge[1]];
            getNode[edge[1]]->parent = getNode[edge[0]];

        }
        // if no child, then its a left child
        else{
            getNode[edge[0]]->left = getNode[edge[1]];
            getNode[edge[1]]->parent = getNode[edge[0]];

        }

        // connection is a child node
        isChild[edge[1]] = true;
    }

    // add costs
    for(int i{0}; i < amount.size(); i++){
        getNode[i]->cost = amount[i];
    }

    // adjust for bob moving through tree
    int step{0};
    TreeNode* bob_node = getNode[bob];
    while(bob_node != nullptr){
        // determine which time step bob visitied on
        bob_node->bob_visit = step;
        step++;

        // move bob up tree
        bob_node = bob_node->parent;
    }
    
    // find root node
    TreeNode* head = NULL;
    for(auto& edge: edges){
        if(isChild[edge[0]] != true){              
            head = getNode[edge[0]]; 
            break;
        }
    }

    return head;
}

// search tree
int Inorder(TreeNode* node, int cost, int& step_count)
{
    // taken step
    step_count++;

    // if root node return
    if (node == NULL) return cost;

    // add cost of node
    int node_level = node->val;
    if(node->bob_visit == step_count) cost += (node->cost)/2;  // bob and alice together
    else if(step_count < node->bob_visit || node->bob_visit == -1) cost += node->cost; // alice visits before bob

    int cost_1{cost};
    int cost_2{cost};

    // search left and right nodes
    if(node->left){
        cost_1 = Inorder(node->left, cost, step_count);
        step_count--;
    } 
    if(node->right){
        cost_2 = Inorder(node->right, cost, step_count);
        step_count--;
    }

    return max(cost_1, cost_2);
}


int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount){
        
    // build the nodes
    TreeNode* head = createTree(edges, bob, amount);

    // perform dfs
    int cost{0};
    int step_count{-1};
    cost = Inorder(head, cost, step_count);

    return cost;
}

int main()
{
    vector<vector<int>> edges = {{0,1},{1,2},{2,3}};
    int bob = 3;
    vector<int> amount = {-5644,-6018,1188,-8502};

    int cost;
    cost = mostProfitablePath(edges, bob, amount);
    cout << cost;





    return 0;
}