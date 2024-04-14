class Solution:
    def jump(self, nums: List[int]) -> int:
        tap_ranges = []
        tap_reachability = [i for i in range(len(nums))]

        for i in range(len(nums)):
            tap_reachability[i] = max(tap_reachability[i], i+nums[i])

        print(tap_reachability)
        num_taps = 0
        curr_reachability = 0
        next_reachability = 0
        for i in range(len(tap_reachability)-1):
            if i > curr_reachability:
                return -1
            
            next_reachability = max(tap_reachability[i],next_reachability)

            if i==curr_reachability:
                num_taps += 1
                curr_reachability = next_reachability
            print(num_taps)
        if len(tap_reachability)-1 > curr_reachability:
            return -1
        return num_taps