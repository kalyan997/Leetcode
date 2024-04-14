# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, None, None)
    
    def validate(self, root, left, right):
        if root is None:
            return True
        if (right is not None and root.val>=right.val) or (left is not None and root.val<=left.val):
            return False
        return self.validate(root.left,left,root) and self.validate(root.right,root,right)
        