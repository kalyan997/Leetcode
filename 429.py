"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        level_order_traversal = []
        if root is None:
            return level_order_traversal

        my_q = deque()
        my_q.append(root)
        #my_q.append(None)
        curr_level = []
        while my_q:
            curr_size = len(my_q)
            curr_level = []
            for i in range(curr_size):
                curr_node = my_q.popleft()
                curr_level.append(curr_node.val)
                for child in curr_node.children:
                    my_q.append(child)
            level_order_traversal.append(curr_level)
        return level_order_traversal
        