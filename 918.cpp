class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int n  = nums.size();
        int max_curr = 0, max_sum = nums[0], min_curr = 0, min_sum = nums[0], total = 0;
        for(int &num: nums){
            max_curr = max(num, num+max_curr);
            max_sum = max(max_curr, max_sum);
            min_curr = min(num, num+min_curr);
            min_sum = min(min_curr, min_sum);
            total += num;
        }
        return max_sum>0?max(max_sum,total-min_sum):max_sum;
    }
};