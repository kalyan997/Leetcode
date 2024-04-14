class Solution {
public:
    bool isPerfectSquare(int num) {
        if(num==0||num==1){
            return true;
        }
        int left = 2, right =num/2;
        long guess_sqrd,mid;
        while(left<=right){
            mid = left +(right-left)/2;
            guess_sqrd = mid*mid;
            if(guess_sqrd == num){
                return true;
            }
            if(guess_sqrd>num){
                right = mid-1;
            }
            else{
                left = mid+1;
            }
        }
        return false;
    }
};