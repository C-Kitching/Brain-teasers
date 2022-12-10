#include <limits>
#include <algorithm>
#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    long long total{0};
    long long result{0};

    long long dfs(TreeNode* root) {
        if (root == nullptr) return 0;

        long long sum = root->val + dfs(root->left) + dfs(root->right);
        result = std::max(result, sum * (total - sum));

        return sum;
    }

    int maxProduct(TreeNode* root) {
        total = dfs(root);
        dfs(root);
        return result % 1000000007;
    }
};

// Function to build a small test tree
TreeNode* buildTestTree() {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->left->left = new TreeNode(4);
    root->left->right = new TreeNode(5);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(7);

    return root;
}

int main() {
    // Build a small test tree
    TreeNode* root = buildTestTree();

    // Use the maxProduct function to find the maximum product of the sum of two subtrees in the test tree
    Solution solution;
    int result = solution.maxProduct(root);

    // Print the result
    std::cout << "Maximum product of the sum of two subtrees: " << result << std::endl;

    return 0;
}
