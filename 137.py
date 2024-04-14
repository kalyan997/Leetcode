"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        
        lookup = {None:None}

        curr = head
        while curr:
            copy = Node(curr.val)
            lookup[curr] = copy
            curr = curr.next
        
        
        curr = head
        while curr:
            copy_curr = lookup[curr]
            copy_curr.next = lookup[curr.next]
            copy_curr.random = lookup[curr.random]
            curr = curr.next
        return lookup[head]