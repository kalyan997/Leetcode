# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = float("-inf")


        def findPathSum(node):
            if node is None:
                return 0
            
            Include_left = max(findPathSum(node.left),0)
            Include_right = max(findPathSum(node.right),0)
            curr_path = max(Include_left,Include_right)
            self.max_path_sum = max(self.max_path_sum, Include_left+Include_right+node.val)
            return max(node.val+Include_left, node.val+Include_right)
                
        findPathSum(root)
        return self.max_path_sum