/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> res;
    vector<int> postorder(Node* root) {
        dfs(root);
        return res; 
    }
    void dfs(Node* root){
        Node* curr = root;
        if(root == NULL){
            return;
        }
        
        //cout<<curr->val<<"\n";
        for(int i=0;i<curr->children.size();i++){
            dfs(curr->children[i]);
        }
        res.push_back(curr->val);
    }
};