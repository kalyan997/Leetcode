class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr_res = []
        curr_sum = 0
        def backtrack(i):
            nonlocal curr_sum
            if curr_sum == target:
                res.append(curr_res.copy())
                return
            if curr_sum>target or i >= len(candidates):
                return
            curr_res.append(candidates[i])
            curr_sum += candidates[i]
            backtrack(i)
            curr_res.pop()
            curr_sum -= candidates[i]
            backtrack(i+1)
            return
        backtrack(0)
        return res