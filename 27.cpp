class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int curr_ind = 0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]!=val){
                nums[curr_ind]=nums[i];
                curr_ind++;
            }
        }
        return curr_ind;
    }
};