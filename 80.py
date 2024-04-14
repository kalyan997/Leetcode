class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        my_map = defaultdict(int)

        for num in nums:
            my_map[num] += 1
        
        curr_ind = 0
        for i in range(len(nums)):
            num = nums[i]
            if i!= 0 and num == nums[i-1]:
                continue
            if my_map[num]>=2:
                nums[curr_ind] = num
                nums[curr_ind+1] = num
                curr_ind += 2
            elif my_map[num]==1:
                nums[curr_ind] = num
                curr_ind += 1
        #print(curr_ind)
        return curr_ind