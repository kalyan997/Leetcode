class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_ind = 1
        
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            nums[curr_ind] = nums[i]
            curr_ind += 1
        #print(curr_ind)
        return curr_ind