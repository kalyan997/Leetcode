class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int n = digits.size();
        
        for(int i=0;i<n;i++){
            int curr_pos = n-1-i;
            if(digits[curr_pos] == 9){
                digits[curr_pos] = 0;
            }
            else{
                digits[curr_pos]+=1;
                return digits;
            }
        }
        vector<int> res;
        res.push_back(1);
        for(int i=0;i<digits.size();i++){
            res.push_back(digits[i]);
        }
        return res;
    }
};