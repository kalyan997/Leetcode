class Solution {
public:
    vector<int> partitionLabels(string s) {
        int n = s.size();
        vector<int> res;
        vector<pair<int,int>> alph_start_end(26,{-1,-1});
        for(int i=0;i<n;i++){
            if(alph_start_end[s[i]-'a'].first==-1){
                alph_start_end[s[i]-'a'].first = i;
            }
            alph_start_end[s[i]-'a'].second = i;
        }
        
        int curr_end = 0, curr_start = 0;
        for(int i=0;i<s.size();i++){
            curr_end = max(curr_end,alph_start_end[s[i]-'a'].second);
            if(i==curr_end){
                res.push_back(i-curr_start+1);
                curr_start = i+1;
            }
        }
        return res;
    }
};