class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        curr_res = []
        def isPalindrome(s,low,high):
            while low<high:
                if s[low] != s[high]:
                    return False
                low += 1
                high -= 1
            return True

        def backtrack(i):
            if i==len(s):
                res.append(curr_res.copy())
            for end in range(i,len(s)):
                if isPalindrome(s,i,end):
                    curr_res.append(s[i:end+1])
                    backtrack(end+1)
                    curr_res.pop()

        backtrack(0)
        return res