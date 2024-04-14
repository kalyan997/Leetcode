# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        
        my_q = deque()
        
        my_q.append(root)
        
        res = root.val
        
        while my_q:
            for i in range(len(my_q)):
                curr = my_q.popleft()
                if curr is None:
                    continue
                if i==0:
                    res = curr.val
                if curr.left:
                    my_q.append(curr.left)
                if curr.right:
                    my_q.append(curr.right)
        
        return res