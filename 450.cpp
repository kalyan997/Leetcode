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
    TreeNode* deleteNode(TreeNode* root, int key) {
         if(root==NULL){
            return nullptr;
        }
        
        if(key>root->val){
            root->right = deleteNode(root->right,key);
        }
        else if(key<root->val){
            root->left = deleteNode(root->left,key);
        }
        else{
            if (root->left == nullptr && root->right == nullptr){
                root = nullptr;
            }
            else if(root->right){
                root->val = InorderSuccessor(root);
                root->right = deleteNode(root->right,root->val);
            }
            else {
                root->val = InorderPredecessor(root);
                root->left = deleteNode(root->left,root->val);
            }
        }
        
        
        
        return root;
    }
    
    
    
    int InorderSuccessor(TreeNode* root){
        root = root->right;
        while(root->left){
            root = root->left;
        }
        return root->val;
    }
    
    int InorderPredecessor(TreeNode* root){
        root = root->left;
        while(root->right){
            root = root->right;
        }
        return root->val;
    }
};