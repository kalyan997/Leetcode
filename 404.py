# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        
        res = 0
        def dfs(root):
            nonlocal res
            #print(root.val)
            if root is None:
                return
            if root.left:
                if root.left.left is None and root.left.right is None:
                    res += root.left.val
                dfs(root.left)
            if root.right:
                dfs(root.right)
        dfs(root)
        return res