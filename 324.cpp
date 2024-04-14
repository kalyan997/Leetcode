class Solution {
public:
    void wiggleSort(vector<int>& nums) {
        int n=nums.size();                    // finding the size of vector
        sort(nums.begin(),nums.end());        // sorting the complete vector
        int arr[n];                           // creating an array of n size
        // now we will first fill all the odd place index(1,3,5,7....etc) of arr with the maximum elements
        // and as the nums is sorted so we will keep traversing from right to left giving us the largest elements
        int i=1;        
        int j=n-1;
        
        // this while loop will basically fill all the odd places in arr
        while(i<n)
        {
            arr[i]=nums[j];
            i=i+2;
            j--;
        }
        // now to fill all the even place index(0,2,4,6.....etc) of arr , we will simply fill the remaining elements of nums from j th index to 0 index
        i=0;
        while(i<n)
        {
            arr[i]=nums[j];
            i=i+2;
            j--;
        }
        
        // copying the array arr into nums vector
        for(int i=0;i<n;i++)
        {
            nums[i]=arr[i];
        }
    }
};