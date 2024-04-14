class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        my_map = {}
        
        for i,num in enumerate(nums):
            if num in my_map and i-my_map[num] <= k:
                return True
            my_map[num] = i
        return False