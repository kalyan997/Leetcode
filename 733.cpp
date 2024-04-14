class Solution {
public:
    vector<vector<int>> new_image;
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
        int color = image[sr][sc];
        int n = image.size();
        int m = image[0].size();
        //vector<vector<int>> new_image1(n,vector<int>(m,0));
        new_image = image;
        dfs(image,sr,sc,newColor);
        return new_image;
    }
    
    void dfs(vector<vector<int>>& image, int sr, int sc, int newColor){
        vector<pair<int,int>> directions;
        directions = {{0,1},{0,-1},{1,0},{-1,0}};
        int rows = image.size();
        int cols = image[0].size();
        new_image[sr][sc] = newColor;
        for(auto dir: directions){
            int next_row = sr+dir.first;
            int next_col = sc+dir.second;
            if(next_row>=0 and next_row<rows and next_col<cols and next_col>=0 and image[next_row][next_col]==image[sr][sc] and new_image[next_row][next_col]!=newColor){
                dfs(image,next_row,next_col,newColor);
            }
        }    
    }
};