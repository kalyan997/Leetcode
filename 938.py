# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        #curr = root
        inorder_res = []
        def inorder(root):
            if root is None:
                return
            inorder(root.left)
            inorder_res.append(root.val)
            inorder(root.right)
        
        inorder(root)
        for curr in inorder_res:
            if curr>high:
                break
            if curr>=low:
                res+=curr
        return res