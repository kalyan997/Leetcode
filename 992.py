class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        left_far = 0
        #left_near = 0
        res = 0
        count = defaultdict(int)
        
        for right in range(len(nums)):
            count[nums[right]] += 1
            
            while len(count) > k:
                count[nums[left_far]] -= 1
                if count[nums[left_far]] == 0:
                    count.pop(nums[left_far])
                left_far += 1
        
            
            left_near = left_far
            prev_count = count
            while count[nums[left_near]] > 1:
                count[nums[left_near]] -= 1
                left_near += 1
            count = prev_count
            
            if len(count) == k:
                res += left_near-left_far+1
            print(res)
            
        return res