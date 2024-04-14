class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        my_map = defaultdict(int)
        res = ""
        for c in s:
            my_map[c] += 1
            if c not in order:
                res += c
        
        for c in order:
            while my_map[c] > 0:
                res += c
                my_map[c]  -= 1
        
        return res