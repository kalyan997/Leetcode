"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        def depth(root):
            if root is None:
                return 0
            max_depth = 0
            for child in root.children:
                max_depth = max(max_depth, depth(child))
            return 1+max_depth
        
        return depth(root)