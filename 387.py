class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        n = len(s)
        res = -1
        my_map = defaultdict(int)
        
        for i in range(n-1,-1,-1):
            if my_map[s[i]] == 0:
                res = i
            my_map[s[i]] += 1
        
        #print(my_map)
        for i,c in enumerate(s):
            if my_map[c] == 1:
                return i
            
        return -1