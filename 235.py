# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parVal = root.val
        pVal = p.val
        qVal = q.val

        if pVal<parVal and qVal<parVal:
            return self.lowestCommonAncestor(root.left,p,q)
        elif pVal>parVal and qVal>parVal:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root