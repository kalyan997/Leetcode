class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map_to_t = {}
        t_taken = set()
        for i in range(len(s)):
            if s[i] not in s_map_to_t:
                if t[i] in t_taken:
                    return False
                s_map_to_t[s[i]] = t[i]
                t_taken.add(t[i])
            else:
                if s_map_to_t[s[i]] != t[i]:
                    return False
        return True
