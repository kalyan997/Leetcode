class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res(nums.size()-k+1);
        vector<int> left(nums.size());
        vector<int> right(nums.size());
        int n = nums.size();
        left[0] = nums[0];
        right[nums.size()-1] = nums[nums.size()-1];
        for(int i=1;i<nums.size();i++){
            if(i%k==0){
                left[i]=nums[i];
            }
            else{
                left[i] = max(left[i-1],nums[i]);
            }
            
            if((n-i-1)%k==0){
                right[n-i-1]=nums[n-i-1];
            }
            else{
                right[n-i-1] = max(right[n-i],nums[n-i-1]);
            }
        }
        for(int i=0;i<n-k+1;i++){
            res[i] = max(left[i+k-1],right[i]);
        }
        return res;
    }
};