class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        unordered_map<int,int> num_nextgreater;
        stack<int> my_stack;
        int ind = 0;
        for(int i=0;i<nums2.size();i++){
            while(!my_stack.empty() and my_stack.top()<nums2[i]){
                num_nextgreater[my_stack.top()] = nums2[i];
                my_stack.pop();
            }
            my_stack.push(nums2[i]);
        }
        
        while(!my_stack.empty()){
            num_nextgreater[my_stack.top()] = -1;
            my_stack.pop();
        }
        for(int i=0;i<nums1.size();i++){
            res.push_back(num_nextgreater[nums1[i]]);
        }
        return res;
    }
};