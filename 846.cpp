class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int n = hand.size();
        if(n%groupSize!=0){return false;}
        unordered_map<int,int> count;
        priority_queue<int, vector<int>, greater<int>> min_heap;
        for(int i=0;i<n;i++){
            count[hand[i]]++;
        }
        for(pair key: count){
            min_heap.push(key.first);
        }
        while(min_heap.size()>0){
            int first = min_heap.top();
            for(int i=0;i<groupSize;i++){
                if(count[first+i]==0){
                    return false;
                }
                count[first+i]--;
                if(count[first+i]==0){
                    if(first+i != min_heap.top()){
                        return false;
                    }
                    min_heap.pop();
                }
            }
        }
        return true;
    }
};