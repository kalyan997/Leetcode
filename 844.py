class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_pointer, t_pointer = len(s)-1, len(t)-1

        while s_pointer >=0 or t_pointer >=0:
            if s[s_pointer]!=t[t_pointer]:
                return False
            if s[s_pointer] == '#':
                s_pointer -= 1
            if t[t_pointer] == '#':
                t_pointer -= 1
            s_pointer -= 1
            t_pointer -= 1
        return True