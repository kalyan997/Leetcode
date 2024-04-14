class Solution {
public:
    int titleToNumber(string columnTitle) {
        int res = 0;
        for(char c: columnTitle){
            int char_val = c-'A'+1;
            res = res*26;
            res = res+char_val;
        }
        return res;
    }
};