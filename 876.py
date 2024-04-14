# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        num_nodes = 0
        
        curr = head
        
        while curr:
            num_nodes += 1
            curr = curr.next
            
        print(num_nodes)
        req_node = num_nodes//2
        
        curr = head
        while req_node > 0:
            curr = curr.next
            req_node -= 1
        
        
        return curr