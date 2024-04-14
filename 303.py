class NumArray:
    def __init__(self, nums: List[int]):
        self.sum_upto = []
        self.nums = []
        for i in range(len(nums)):
            if i==0:
                self.sum_upto.append(nums[i])
            else:
                self.sum_upto.append(self.sum_upto[i-1]+nums[i])
            self.nums.append(nums[i])
            


    def sumRange(self, left: int, right: int) -> int:
       #print(self.nums)
       #print(self.sum_upto)
       return self.sum_upto[right]-self.sum_upto[left]+self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)