class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        N = len(num)
        stack = []
        
        for c in num:
            while len(stack) >= 1 and stack[-1] > c and k > 0:
                stack.pop()
                k -= 1
            stack.append(c)
            print(stack)
            
        while k>0 and len(stack)>0:
            stack.pop()
            k-=1
            
        if len(stack) == 0:
            return "0"
        
        r = "".join(stack).lstrip("0")
        
        if len(r) == 0:
            return "0"
        
        return r