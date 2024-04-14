class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int inflection_index=0;
        int n= nums.size();
        for(int i=0;i<nums.size();i++){
            if(i!=0 and nums[i]<nums[i-1]){
                inflection_index = i;
            }
        }
        int tar_index;
        cout<< inflection_index<<"\n";
        if(inflection_index!=0){
            if(target<nums[inflection_index]){
                return false;
            }
            if(target>=nums[inflection_index] && target<nums[0]){
                 tar_index = Bin_search(target,nums,inflection_index,n-1);
            }
            else{
                tar_index = Bin_search(target,nums,0,inflection_index-1);
            }
        }
        if(inflection_index==0){tar_index = Bin_search(target,nums,0,n-1);}
        cout<<tar_index<<"\n";
        return tar_index==-1?false:true;
    }
    
    int Bin_search(int target,vector<int>& nums,int left,int right) {       
        //int left = 0;
        //int right = nums.size()-1;
        
        while(left <= right) {
            int mid = left + (right-left)/2;
            if(nums[mid] < target) {
                left = mid+1;
            } else if(nums[mid] > target) {
                right = mid-1;
            } else {
                return mid;
            }
        }
        
        return -1;
    }
};