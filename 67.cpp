class Solution {
public:
    string addBinary(string a, string b) {
        string res = "";
        int carry = 0;
        reverse(a.begin(),a.end());
        reverse(b.begin(),b.end());
        for(int i=0;i<max(a.size(),b.size());i++){
            int digit1,digit2;
            if(i<a.size()){
                 digit1 = a[i]-'0';
            }
            else{
                digit1 = 0;
            }
            if(i<b.size()){
                 digit2 = b[i]-'0';
            }
            else{
                 digit2 = 0;
            }
            
            int curr_sum = digit1+digit2+carry;
            string final_digit = to_string(curr_sum%2);
            res = final_digit+res;
            carry = curr_sum/2;
        }
        if(carry){
            res = "1"+res;
        }
        
        return res;
    }
};