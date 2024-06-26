class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m = obstacleGrid.size();
        int n = obstacleGrid[0].size();
        
        //int dp[m][n];
        
        obstacleGrid[0][0] = obstacleGrid[0][0]?0:1;
        
        for(int i=1;i<n;i++){
            obstacleGrid[0][i] = obstacleGrid[0][i]?0:obstacleGrid[0][i-1];
        }
        
        for(int i=1;i<m;i++){
            obstacleGrid[i][0] = obstacleGrid[i][0]?0:obstacleGrid[i-1][0];
        }
        
        
        
        for(int i=1;i<m;i++){
            for(int j=1;j<n;j++){ 
                obstacleGrid[i][j] = obstacleGrid[i][j]?0:obstacleGrid[i-1][j] +obstacleGrid[i][j-1];
            }
        }
        
        
        return obstacleGrid[m-1][n-1];
    }
};