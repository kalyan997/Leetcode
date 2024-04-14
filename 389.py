class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = defaultdict(int)
        for c in s:
            letters[c] += 1

        for c in t:
            letters[c] -= 1
        
        for key, val in letters.items():
            if val != 0:
                return key