class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        my_map = {}

        for i in range(len(nums)):
            if nums[i] not in my_map:
                my_map.add(nums[i], 1)
            else:
                my_map[nums[i]] += 1
        
        
        return False


    nums = [1,2,3,5,9,10,10]
    containsDuplicate(nums)

    bums = [1,1,1]