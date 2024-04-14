class Solution {
public:
    string decodeString(string s) {
        string res = "";
        stack<char> stack;
        for(int i=0;i<s.size();i++){
            if(s[i]==']'){
                string decoded_string = "";
                while( stack.top()!= '[' ){
                    decoded_string += stack.top();
                    stack.pop();
                }
                stack.pop();
                
                int base = 1;
                int k = 0;
                while (!stack.empty() && isdigit(stack.top())) {
                    k = k + (stack.top() - '0') * base;
                    stack.pop();
                    base *= 10;
                }
                while(k!=0){
                    for (int j = decoded_string.size() - 1; j >= 0; j--) {
                        stack.push(decoded_string[j]);
                    }
                    k--;
                }
            }
            else{
                stack.push(s[i]);
            } 
        }
        
        while(!stack.empty()) {
            res = stack.top() + res;
            stack.pop();
        }
        return res;
    }
};