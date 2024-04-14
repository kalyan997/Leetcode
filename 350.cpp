class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        unordered_map<int,int> nums_count1;
        //unordered_map<int,int> nums_count2;
        for(int num:nums1){
            nums_count1[num]++;
        }
        for(int num:nums2){
            if(nums_count1[num]!=0){
                res.push_back(num);
                nums_count1[num]--;
            }
        }
        return res;
    }
};