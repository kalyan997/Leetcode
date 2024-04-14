class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        n = len(s)
        my_map = defaultdict(int)
        
        for c in s:
            my_map[c] += 1
        
        res = 0
        has_odd  = 0
        for key, val in my_map.items():
            if val%2 == 0:
                res += val
            else:
                has_odd = 1
                res = res+val-1
        #print(my_map)
        return res+1 if has_odd==1 else res