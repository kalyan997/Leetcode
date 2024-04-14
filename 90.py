class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        power_set_without_duplicates = []
        curr_subset = []
        nums.sort()
        def backtrack(i):
            if i==len(nums):
                power_set_without_duplicates.append(curr_subset.copy())
                return
            curr_subset.append(nums[i])
            backtrack(i+1)
            curr_subset.pop()
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i+=1
            backtrack(i+1)
            return
        backtrack(0)
        return power_set_without_duplicates