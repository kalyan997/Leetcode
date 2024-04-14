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
    int widthOfBinaryTree(TreeNode* root) {
        if(root == nullptr){
            return 0;
        }
        queue<pair<TreeNode*,int>> my_q;
        long long maxWidth = 1;
        my_q.push({root, 0});
        while(!my_q.empty()){
            //Pair<TreeNode, Integer> head = queue.getFirst();
            pair<TreeNode*,long long> head = my_q.front();
            int currLevelSize = my_q.size();
            pair<TreeNode*,long long> curr_ele;
            //maxWidth = max(maxWidth,curr_ele.second - head.second +1);
            for(int i=0;i<currLevelSize;i++){
                curr_ele = my_q.front();
                my_q.pop();
                TreeNode* node = curr_ele.first;
                if (node->left != nullptr){
                    my_q.push({node->left,2*curr_ele.second+1});
                }
                if (node->right != nullptr){
                    my_q.push({node->right,2*curr_ele.second+2});
                }
            }
            maxWidth = max(maxWidth,curr_ele.second - head.second +1);
        }
        return (int)maxWidth;
    }
};
