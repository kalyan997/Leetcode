class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr_res = []
        curr_sum = 0
        candidates.sort()
        def backtrack(i):
            nonlocal curr_sum
            if curr_sum == target:
                res.append(curr_res.copy())
                return
            if curr_sum>target or i >= len(candidates):
                return
            curr_res.append(candidates[i])
            curr_sum += candidates[i]
            backtrack(i+1)
            curr_res.pop()
            while i+1<len(candidates) and candidates[i+1]==candidates[i]:
                i += 1
            curr_sum -= candidates[i]
            backtrack(i+1)
            return
        backtrack(0)
        return res