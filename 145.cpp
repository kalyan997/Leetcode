/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> post_order;
    vector<int> postorderTraversal(TreeNode* root) {
        postorder_traversal(root);
        return post_order;
    }
    void postorder_traversal(TreeNode* root){
        if(root==nullptr){
            return;
        }
        
        postorder_traversal(root->left);
        postorder_traversal(root->right);
        post_order.push_back(root->val);
    }
};