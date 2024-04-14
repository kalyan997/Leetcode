class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        subsets = []
        #curr_subset = []
        def backtrack(nums, i, curr_subset):
            if i >= len(nums):
                subsets.append(curr_subset.copy())
                return
            curr_subset.append(nums[i])
            backtrack(nums, i+1, curr_subset)
            curr_subset.pop()
            backtrack(nums, i+1, curr_subset)
        
        backtrack(nums, 0, [])
        return subsets