class Solution {
public:
    int compress(vector<char>& chars) {
        int left = 0;
        int right = 0;
        int curr_ind = 0;
        int count;
        if(chars.size()<=1){
            return chars.size();
        }
        while(right<chars.size()){
            count = 0;
            while(right<chars.size() and chars[left]==chars[right]){
                count++;
                cout<<count<<"\n";
                right++;
            }
            cout<<count<<"\n";
            cout<<chars[left]<<" L:"<<left<<" R:"<<right<<" Count:"<<count<<"\n";
            if(count == 1){
                chars[curr_ind] = chars[left];
                curr_ind++;
            }
            else if(count>1 and count<10){
                chars[curr_ind] = chars[left];
                curr_ind++;
                chars[curr_ind] = '0'+count;
                curr_ind++;
            }
            else if(count>=10){
                chars[curr_ind] = chars[left];
                curr_ind++;
                for(char curr_char: to_string(count)){
                    chars[curr_ind] = curr_char;
                    curr_ind++;
                }
            }
            cout<<chars[left]<<" L:"<<left<<" R:"<<right<<" Count:"<<count<<"\n";
            left = right;
        }
        return curr_ind;
    }
};