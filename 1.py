class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        my_map = {} 
        for i in range(n):
            if nums[i] not in my_map:
                my_map[nums[i]] = i
            else:
                my_map[nums[i]] += 1
        for i in range(n):
            rem_target = target - nums[i]
            if my_map[rem_target] >0:
                return [nums[i], rem_target]
            