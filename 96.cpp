class Solution {
public:
    int numTrees(int n) {
        vector<int> num_trees(n+1,0);
        num_trees[0] = 1;
        num_trees[1] = 1;
        for(int i=2;i<=n;i++){
           for(int j=1;j<=i;j++){
                num_trees[i] += num_trees[j-1] * num_trees[i-j];
           }
        }
        return num_trees[n];
    }
};