# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        
        def dfs(root, curr_res):
            if root is None:
                return
            
            curr_res += str(root.val) + "->"
            if root.left:
                dfs(root.left, curr_res)
            if root.right:
                dfs(root.right, curr_res)
                
            final_res = curr_res[:len(curr_res)-2]
            if not root.left and not root.right:
                
                res.append(final_res)

        dfs(root, "")
        return res