class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_p, close_p = 0, 0
        parenthesis = []
        curr_paren = []

        def backtrack():
            nonlocal open_p, close_p
            if open_p == n and close_p ==n:
                parenthesis.append("".join(curr_paren))
                return
            if open_p<n:
                curr_paren.append('(')
                open_p += 1
                backtrack()
                curr_paren.pop()
                open_p -= 1
            if close_p<n and open_p>close_p:
                curr_paren.append(')')
                close_p += 1
                backtrack()
                curr_paren.pop()
                close_p -= 1


        backtrack()
        return parenthesis
        