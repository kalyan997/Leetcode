class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs = []
        curr_comb = []
        curr_sum = 0
        def backtrack(i):
            nonlocal curr_sum
            if len(curr_comb)==k and curr_sum==n:
                combs.append(curr_comb.copy())
                return
            if curr_sum > n or len(curr_comb)>k or i>9:
                return
            curr_comb.append(i)
            curr_sum+=i
            backtrack(i+1)
            curr_comb.pop()
            curr_sum -=i
            backtrack(i+1)

        backtrack(1)
        return combs