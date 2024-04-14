# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        
        def inorder(root, left, right):
            nonlocal res
            #print(root.val, left, right, res)
            if root is None:
                return
            res = min(min(abs(root.val-left),abs(root.val-right)), res)
            if root.left:
                inorder(root.left, left, root.val)
            if root.right:
                inorder(root.right, root.val, right)
            
            
        inorder(root, float("-inf"), float("inf"))
        return res 