# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        sentinal_node = ListNode(-1)
        sentinal_node.next = head
        # Traverse LinkedList and count total number of nodes
        num_nodes = 0
        
        curr = head
        while curr:
            num_nodes += 1
            curr = curr.next
        
        req_node = num_nodes - n
        #print(num_nodes)
        #print(req_node)
        curr_node = 0
        curr = sentinal_node
        while curr_node < req_node and curr:
            curr_node += 1
            print(curr_node, curr.val)
            curr = curr.next
            
        if curr.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        
        return sentinal_node.next
            