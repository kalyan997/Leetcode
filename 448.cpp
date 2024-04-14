class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums)
{
        int n = nums.size();
        //vector<int> num_freq(n+1,0);
        vector<int> res;
        for(int i=0;i<n;i++){
            int ind = abs(nums[i])-1;
            if(nums[ind]>0){
                nums[ind] *= -1;
            }
        }
        for(int i=1;i<=n;i++){
            if(nums[i-1]>0){
                res.push_back(i);
            }
        }
        return res;
    }