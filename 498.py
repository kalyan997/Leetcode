class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        res = []
        nums = mat
        rows = len(nums)

        cols = 0
        for num in nums:
            cols = max(len(num),cols)

        #print(rows,cols)
        diag_sum = defaultdict(list)
        for i in range(rows-1,-1,-1):
            for j in range(len(nums[i])):
                if (i+j)%2 == 0:
                    diag_sum[i+j].append(nums[i][j])
        
        for i in range(0,rows):
            for j in range(len(nums[i])):
                if (i+j)%2 != 0:
                    diag_sum[i+j].append(nums[i][j])


        for i in range(0,rows+cols-1):
            for curr in diag_sum[i]:
                res.append(curr)
        return res