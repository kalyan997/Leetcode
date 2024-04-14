class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1_set = set()
        intersection = set()
        
        for num in nums1:
            nums1_set.add(num)
            
        for num in nums2:
            if num in nums1_set and num not in intersection:
                intersection.add(num)
        return list(intersection)