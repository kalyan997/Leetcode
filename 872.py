# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leaf(root,leaves):
            if root is None:
                return
            if root.left is None and root.right is None:
                leaves.append(root.val)
            get_leaf(root.left,leaves)
            
            get_leaf(root.right,leaves)
            return leaves
        
        return get_leaf(root1,[])==get_leaf(root2,[])