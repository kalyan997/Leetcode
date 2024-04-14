class Solution:
    def isValid(self, s: str) -> bool:
        my_map = {'(':')','{':'}', '[':']'}
        stack = []
        for c in s:
            if c in my_map:
                stack.append(my_map[c])
            elif len(stack)==0:
                return False
            elif c==stack[-1]:
                stack.pop()
            else:
                return False
        return len(stack)==0