# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
       
        
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, curr_height):
            if root.left is None and root.right is None:
                return curr_height
            res = 2**31
            if root.right:
                res = min(res,dfs(root.right,curr_height+1))
            if root.left:
                res = min(res,dfs(root.left,curr_height+1))
            return res
            
            
        
        if root is None:
            return 0
        
        return dfs(root,1)