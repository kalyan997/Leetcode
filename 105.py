# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        
        def arrayToTree(left,right):
            nonlocal curr_preorder_index
            if left>right:
                return None
            root_val = preorder[curr_preorder_index]
            root = TreeNode(root_val)
            curr_preorder_index += 1
            root.left = arrayToTree(left,InorderIndex[root_val]-1)
            root.right = arrayToTree(InorderIndex[root_val]+1,right)
            return root
        curr_preorder_index = 0
        InorderIndex = {}
        for index,value in enumerate(inorder):
            InorderIndex[value] = index
        return arrayToTree(0,len(preorder)-1)

