class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res_matrix(n,vector<int>(n,0));
        vector<pair<int,int>> directions;
        directions.push_back({0,1});
        directions.push_back({1,0});
        directions.push_back({0,-1});
        directions.push_back({-1,0});
        
        int curr_dir = 0;
        int i = 0;
        int j = 0;
        //vector<int> spiral_matrix;
        //spiral_matrix.push_back(matrix[0][0]);
        int curr =1;
        res_matrix[0][0] = curr;
        curr++;
        int chng_dir = 0;
        while(chng_dir<2){
            while((i + directions[curr_dir].first)>=0 && (j + directions[curr_dir].second)>=0 && (i + directions[curr_dir].first)<n && (j + directions[curr_dir].second)<n && res_matrix[i+ directions[curr_dir].first][j+ directions[curr_dir].second]==0){
                chng_dir = 0;
                i += directions[curr_dir].first;
                j += directions[curr_dir].second;
                //spiral_matrix.push_back(matrix[i][j]);
                res_matrix[i][j] = curr;
                curr++;
            }
            curr_dir = (curr_dir+1)%4;
            chng_dir++;
        }
        return res_matrix;
    }
};