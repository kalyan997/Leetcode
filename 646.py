class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        chain_len = 1
        pairs.sort()
        prev_start = pairs[0][0]
        prev_end = pairs[0][1]
        for i in range(1,len(pairs)):
            curr = pairs[i]
            if curr[0]<=prev_end:
                prev_end = min(prev_end,curr[1])
            else:
                prev_end = curr[1]
                chain_len += 1
        return chain_len