class Solution {
public:
   bool checkPossibility(vector<int>& nums) {
        int n =  nums.size();
        if(n==1){
            return true;
        }
        int ind = -1;
    
        for(int i=0;i<n-1;i++){
            if(nums[i+1]<nums[i]){
                if(ind == -1){
                    ind = i;
                }
                else{
                    return false;
                }
            }
        }
        if(ind <= 0 || ind == n-2){
            return true;
        }
        else{
            return nums[ind-1]<=nums[ind+1] || nums[ind] <= nums[ind+2];
        }

    }
};