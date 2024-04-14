class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        curr_permutation = []
        used = [0]*len(nums)
        def backtrack():
            if len(curr_permutation)==len(nums):
                permutations.append(curr_permutation.copy())
                return
            for i in range(len(nums)):
                if used[i]==0:
                    curr_permutation.append(nums[i])
                    used[i] = 1
                    backtrack()
                    curr_permutation.pop()
                    used[i] = 0
            return
            
        backtrack()
        return permutations