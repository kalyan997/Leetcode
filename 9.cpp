class Solution {
public:
    bool isPalindrome(int x) {
        
        if(x==0){
            return true;
        }
        if(x<0 || x%10==0){
            return false;
        }
        int x_copy = x;
        int res=0;
        while(x>res){
            int curr_digit = x%10;
            res = res*10+curr_digit;
            x = x/10;
        }
        
        return x==res || x==res/10;
    }
};