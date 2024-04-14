class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_map = {}
        longest_streak = 0

        for num in nums:
            my_map[num] = 1

        for num in nums:
            if num-1 not in my_map:
                curr_streak = 1
                curr_num = num

                while curr_num+1 in my_map:
                    curr_streak += 1
                    curr_num += 1

                longest_streak = max(longest_streak, curr_streak)
        
        return longest_streak