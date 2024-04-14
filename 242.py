class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            char_count[s[i]] += 1
            char_count[t[i]] -= 1

        for i in range(len(s)):
            if char_count[s[i]]!= 0:
                return False
        return True