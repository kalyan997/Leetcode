class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        nums = []
        for i in range(1,n+1):
            nums.append(i)
        #curr_subset = []
        def backtrack(nums, i, curr_subset):
            if len(curr_subset)==k:
                combinations.append(curr_subset.copy())
                return
            if i>=len(nums):
                return
            curr_subset.append(nums[i])
            backtrack(nums, i+1, curr_subset)
            curr_subset.pop()
            backtrack(nums, i+1, curr_subset)
        
        backtrack(nums, 0, [])
        return combinations