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
    bool isSymmetric(TreeNode* root) {
        queue<TreeNode*> my_q;
        my_q.push(root);
        my_q.push(root);
        while(!my_q.empty()){
            TreeNode* r1 = my_q.front();
            my_q.pop();
            TreeNode* r2 = my_q.front();
            my_q.pop();
            if(r1==NULL and r2==NULL){
                continue;
            }
            if(r1==NULL or r2==NULL){
                return false;
            }
            if(r1->val!=r2->val){
                return false;
            }
            my_q.push(r1->left);
            my_q.push(r2->right);
            my_q.push(r1->right);
            my_q.push(r2->left);
        }
        return true;
    }
};