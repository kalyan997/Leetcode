class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> res;
        for(int curr=left;curr<=right;curr++){
            int num = curr;
            bool flag = true;
            while(num>0){
                int digit = num%10;
                if(digit==0){
                    flag = false;
                    break;
                }
                if(curr%digit!=0){
                    flag = false;
                    break;
                }
                num = num/10;
            }
            if(flag==true){
                res.push_back(curr);
            }
        }
        return res;
    }
};