# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root==None:
            return True
            
        def height(root):
            if root==None:
                return -1
            return max(height(root.left),height(root.right))+1

        leftHeight = height(root.left)
        rightHeight = height(root.right)
        return (self.isBalanced(root.left) and self.isBalanced(root.right)) and abs(leftHeight-rightHeight)<2 