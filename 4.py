class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        total = m + n
        low = 0
        high = m
        result = 0.0
        
        while low <= high:
            # nums1
            i = low + (high - low) // 2
            # nums2
            j = (total + 1) // 2 - i
            
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                if total % 2 == 0:
                    result = (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    result = max(left1, left2)
                break
            elif left1 > right2:
                high = i - 1
            else:
                low = i + 1
        
        return result        