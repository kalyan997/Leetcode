class MinStack {
public:
    vector<pair<int,int>> min_stack;
    int min_num = INT_MAX;
    MinStack() {
        
    }
    
    void push(int val) {
        if(min_stack.size()==0){
            min_num = val;
            min_stack.push_back({val,min_num});
        }
        else{
            min_num = min(min_stack[min_stack.size()-1].second,val);
            min_stack.push_back({val,min_num});
        }
    }
    
    void pop() {
        min_stack.pop_back();
    }
    
    int top() {
        return min_stack[min_stack.size()-1].first;
    }
    
    int getMin() {
        return min_stack[min_stack.size()-1].second;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */