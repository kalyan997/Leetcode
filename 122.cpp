class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        
        int curr_min = INT_MAX, curr_max = INT_MIN, profit = 0;
        for(int i=0;i<n;i++){
            if(prices[i]<= curr_min){
                curr_min = prices[i];
            }else{
                profit += (prices[i]-curr_min);
                curr_min = prices[i];
            }
        }
        return profit;
    }
};