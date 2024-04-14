class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int n = nums.size();

        int N = 10001;
        int sum_upto[N];
        int dp[N];
        memset(sum_upto,0,sizeof(sum_upto));
        memset(dp,0,sizeof(dp));
        
        for(int i : nums){
            sum_upto[i] += i;
        }

        dp[0] = 0;
        dp[1] = sum_upto[1];


        for(int i=2; i<N; i++){
            dp[i] = max(dp[i-1],dp[i-2]+sum_upto[i]);
        }
        return dp[N-1];
    }
};