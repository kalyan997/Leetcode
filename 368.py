class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        dp = [[1,-1] for i in range(n)]
        
        if n == 1:
            return nums
        
        nums.sort()
        
        max_index = -1
        max_val = 0
        for i in range(n):
            for j in range(i+1,n):
                
                if nums[j]%nums[i] == 0:
                    if dp[j][0] < 1+dp[i][0]:
                        dp[j][0] = 1+dp[i][0]
                        dp[j][1] = i
               
                if dp[j][0] > max_val:
                    max_index = j
                    max_val = dp[j][0]
                    
                #print(i,j,nums[i],nums[j],dp)
        #print(dp)     
        
        res = []
        curr = max_index
        
        while curr != -1:
            res.append(nums[curr])
            curr = dp[curr][1]
        #print(res)
        return res