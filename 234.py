# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        curr = head
        ele = []
        while curr:
            ele.append(curr.val)
            curr = curr.next
            
        left, right = 0, len(ele)-1
        
        while left < right:
            if ele[left] != ele[right]:
                return False
            left += 1
            right -= 1
            
        return True
        