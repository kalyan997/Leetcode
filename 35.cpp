class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<vector<int>> rows(9, vector<int> (9));
        vector<vector<int>> cols(9, vector<int> (9));
        vector<vector<int>> grids(9, vector<int> (9));
        
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                char val = board[i][j];
                int pos = board[i][j] - '1';
                if(val == '.'){continue;}
                
                if(rows[i][pos]==1){return false;}
                rows[i][pos] = 1;
                
                if(cols[j][pos]==1){return false;}
                cols[j][pos] = 1;
                
                int ind = (i/3)*3+(j/3);
                if(grids[ind][pos]==1){return false;}
                grids[ind][pos] = 1;
            }
        }
        return true;
    }
    
};