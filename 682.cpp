class Solution {
public:
    int calPoints(vector<string>& operations) {
        stack<int> my_stack;
        for(auto operation: operations){
            if(operation == "+"){
                int top1 = my_stack.top();
                my_stack.pop();
                int top2 = my_stack.top();
                my_stack.pop();
                int val = top1+top2;
                my_stack.push(top2);
                my_stack.push(top1);
                my_stack.push(val);
            }
            else if(operation == "D"){
                my_stack.push(2*my_stack.top());
            }
            else if(operation == "C"){
                my_stack.pop();
            }
            else{
                my_stack.push(stoi(operation));
            }
        }
        int res = 0;
        while(!my_stack.empty()){
            res += my_stack.top();
            my_stack.pop();
        }
        return res;
    }
};