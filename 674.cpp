class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int n = nums.size();
        int start = 0;
        int end = 0;
        int res = 0;
        while(end<n){
            if(end>0 && nums[end-1] >= nums[end]){
                start = end;
            }
            res = max(res,end-start+1);
            end++;
        }
        return res;
    }
};