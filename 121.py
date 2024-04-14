class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_min = float('inf')
        for num in prices:
            res = max(res, num-curr_min)
            curr_min = min(curr_min,num)
        return res