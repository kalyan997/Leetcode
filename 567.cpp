class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int len_s1 = s1.size();
        int len_s2 = s2.size();
        if(len_s2 < len_s1){return false;}
        vector<int> char_count_s1(26,0);
        vector<int> char_count_s2(26,0);
        for(int i=0;i<len_s1;i++){
            char_count_s1[s1[i]-'a']++;
            char_count_s2[s2[i]-'a']++;
        }
        int count=0;
        for (int i = 0; i < 26; i++) {
            if (char_count_s1[i] == char_count_s2[i])
                count++;
        }
        
        int left = 0;
        int right = len_s1;
        while(right<len_s2){
            if(count==26){
                return true;
            }
            int ind = s2[right]-'a';
            char_count_s2[ind]++;
            if(char_count_s1[ind]==char_count_s2[ind]){
                count++;
            }
            else if(char_count_s1[ind]+1==char_count_s2[ind]){
                count--;
            }
            
            ind = s2[left]-'a';
            char_count_s2[ind]--;
            if(char_count_s1[ind]==char_count_s2[ind]){
                count++;
            }
            else if(char_count_s1[ind]-1==char_count_s2[ind]){
                count--;
            }
            left++;
            right++;
        }
          
        return count==26;
    }
};