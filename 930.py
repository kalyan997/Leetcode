class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        prefix = [0]*len(nums)
        suffix = [0]*len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
                suffix[len(nums)-1-i] = nums[len(nums)-1]
            else:
                prefix[i] = prefix[i-1] + nums[i]
                suffix[len(nums)-1-i] = suffix[len(nums)-i]+nums[len(nums)-1-i]
        
        res = 0
        my_map = defaultdict(int)
        my_map[0] = 1
        for i in range(len(nums)):
            if my_map[prefix[i]-goal] != 0:
                res += my_map[prefix[i]-goal]
            my_map[prefix[i]] += 1   
        return res        