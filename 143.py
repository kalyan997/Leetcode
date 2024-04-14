# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast, slow = head, head
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next

        temp, prev, curr = None, None, slow
        while curr!=None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, second = head, prev
        while second.next!=None:
            temp = first.next
            first.next = second
            first = temp

            temp = second.next
            second.next = first
            second = temp