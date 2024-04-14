# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        def inorder_helper(root):
            if root is None:
                return
            inorder_helper(root.left)
            inorder.append(root.val)
            inorder_helper(root.right)
        inorder_helper(root)
        return inorder

    