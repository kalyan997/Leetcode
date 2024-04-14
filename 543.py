# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
    
        def longestPath(root):
            if root==None:
                return 0
            nonlocal diameter
            leftPath = longestPath(root.left)
            rightPath = longestPath(root.right)
            diameter = max(diameter, leftPath + rightPath)
            return max(leftPath,rightPath)+1

        longestPath(root)
        return diameter