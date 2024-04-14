class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> num_str;
        string res = "";
        for(auto i: nums){
            num_str.push_back(to_string(i));
        }
        sort(num_str.begin(),num_str.end(), [](string &s1, string &s2){ return s1+s2>s2+s1; });
        for(auto s:num_str)
            res+=s;
        while(res[0]=='0' && res.length()>1)
            res.erase(0,1);
        return  res;
    }
    
    
};