class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int left1 = m-1, left2 = n-1;
        int ind=m+n-1;
        while(left1>=0 and left2>=0){
            if(nums1[left1]>nums2[left2]){
                nums1[ind] = nums1[left1];
                left1--;
            }
            else{
                nums1[ind] = nums2[left2];
                left2--;
            }
            ind--;
        }
        while(left1>=0){
            nums1[ind] = nums1[left1];
            left1--;
            ind--;
        }
        while(left2>=0){
            nums1[ind] = nums2[left2];
            left2--;
            ind--;
        }
    }
};