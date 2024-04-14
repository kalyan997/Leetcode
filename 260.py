class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        x = 0
        y = 0
        my_list = [ ]
        for i in range(0,len(nums)):
            xor = xor ^ nums[i]
        set_bit_no = xor & -xor
        
        for i in range(len(nums)):
            if nums[i] & set_bit_no:
                x = x  ^ nums[i]
            else:
                y = y ^ nums[i]
        my_list.append(x)
        my_list.append(y)
        return my_list