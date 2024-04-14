# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        num_nodes = 0
        
        def dfs(root):
            nonlocal num_nodes
            if root is None:
                return
            num_nodes += 1
            if root.left:
                dfs(root.left)
            if root.right:
                dfs(root.right)
        
        dfs(root)
        
        return num_nodes