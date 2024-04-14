class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD=10**9+7
        stack=[-1] 
        res=0
        arr.append(0)
        for i,val in enumerate(arr):
            while stack and val<arr[stack[-1]]:
                index=stack.pop()
                left=index-stack[-1] 
                right=i-index
                res+=(right*left*arr[index])%MOD
            stack.append(i)
        
        return res%MOD