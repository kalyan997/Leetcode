class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        operations = {'+','-','/','*'}
        
        stack = []
        for c in tokens:
            if c not in operations:
                stack.append(int(c))
            else:
                right_operand = stack.pop()
                left_operand = stack.pop()
                curr = 0
                if c == '+':
                    curr = left_operand + right_operand
                elif c == '-':
                    curr = left_operand - right_operand
                elif c=='*':
                    curr = left_operand * right_operand
                else:
                    curr = int(left_operand / right_operand)
                stack.append(curr)
                
        return stack[0]