# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        sentinal = ListNode(-1)
        sentinal.next = head
        
        hare, turtle = head, sentinal
        
        while hare and hare.next:
            if hare == turtle:
                return True
            turtle = turtle.next
            hare = hare.next.next
        
        return False