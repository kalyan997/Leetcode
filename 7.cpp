class Solution {
public:
    int reverse(int x) {
        //int sign_bit = x&(1<<31);
        int rev_no = 0;
        int digit;
        int sign = 0;
        while(x!=0){
            digit = x%10;
            if((rev_no>INT_MAX/10) || ((rev_no==INT_MAX/10) && digit >INT_MAX%10)){return 0;}
            if((rev_no<INT_MIN/10) || ((rev_no==INT_MIN/10) && digit <INT_MIN%10)){return 0;}
            rev_no = (rev_no*10)+digit;
            x = x/10;
        }
        return rev_no;
        
    }
};