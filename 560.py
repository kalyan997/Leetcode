class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr_sum = 0
        my_map = {}
        my_map[0] = 1
        
        for num in nums:
            curr_sum += num
            if curr_sum-k in my_map:
                res += my_map[curr_sum-k]
            
            if curr_sum in my_map:
                my_map[curr_sum] += 1
            else:
                my_map[curr_sum ] = 1
            
        return res