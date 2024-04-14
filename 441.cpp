class Solution {
public:
    int arrangeCoins(int n) {
        long left = 0, right=n;
        long mid,curr_sum;
        while(left <= right){
            mid = left + (right-left)/2;
            curr_sum = mid * (mid+1)/2;
            if(curr_sum==n){
                return (int)mid;
            }
            if(n<curr_sum){
                right = mid-1;
            }
            else{
                left = mid+1;
            }
        }
        return (int)right;
    }
};