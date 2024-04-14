class Solution {
public:
    int strStr(string haystack, string needle) {
        int needle_size = needle.size();
        int haystack_size = haystack.size();
        if(needle_size>haystack_size){
            return -1;
        }
        for(int i=0;i<=haystack_size-needle_size;i++){
            if(haystack.substr(i,needle_size)==needle){
                return i;
            }
        }
        return -1;
    }
};