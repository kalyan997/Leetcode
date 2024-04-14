class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string res = "";
        for(int i=0;i<strs[0].size();i++){
            for(string curr_str: strs){
                if(i==curr_str.size()||strs[0][i]!=curr_str[i]){
                    return res;
                }
            }
            res+=strs[0][i];
        }
        return res;
    }
};