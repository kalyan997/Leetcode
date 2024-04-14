class Solution {
public:
    bool isMatch(string s, string p) {
        vector<vector<bool>> dp(s.size() + 1, vector<bool>(p.size() + 1, false));
        dp[0][0] = true;
        dp[0][1] = (p[0]=='*');
        for(int i=2;i<=p.size();i++){
            if(p[i-1]=='*' and dp[0][i-1]){
                dp[0][i] = true;
            }
        }
        for(int i=1;i<=s.size();i++){
            for(int j=1;j<=p.size();j++){
                if(p[j-1]==s[i-1] || p[j-1]=='?'){
                    dp[i][j] = dp[i-1][j-1];
                }
                else if(p[j-1]=='*'){
                    dp[i][j] = dp[i-1][j]||dp[i][j-1];
                }
                else{
                    dp[i][j] = false;
                }
                
            }
        }
        return dp[s.size()][p.size()];
    }
};