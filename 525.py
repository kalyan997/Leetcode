class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        
        num_zeros = 0
        num_ones = 0
        ones_map_diff = {}
        #zeros_map = defaultdict(int)
        
        max_len = 0
        for i, num in enumerate(nums):
            if num == 0:
                num_zeros += 1
            else:
                num_ones += 1
            if num_zeros == num_ones:
                curr_len = i+1
            else:
                diff = num_ones-num_zeros
                if diff not in  ones_map_diff:
                    ones_map_diff[diff] = i
                curr_len = i-ones_map_diff[diff]
            max_len = max(curr_len, max_len)
            #print(i, num_zeros, num_ones, max_len)
            
        return max_len