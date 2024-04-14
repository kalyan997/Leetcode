class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        left = 0
        my_map = {}
        max_count = 0
        for right in range(n):
            my_map[s[right]] = my_map.get(s[right],0)+1
            max_count = max(max_count,my_map[s[right]])
            if right-left+1-max_count>k:
                my_map[s[left]]-=1
                left += 1
            res = max(res,right-left+1)
        return res