# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        my_q = deque()
        my_q.append(root)
        if root is None:
            return res
        while my_q:
            curr_len = len(my_q)
            curr_max = float("-inf")
            for i in range(curr_len):
                curr = my_q.popleft()
                curr_max = max(curr_max,curr.val)
                if curr.left:
                    my_q.append(curr.left)
                if curr.right:
                    my_q.append(curr.right)
            res.append(curr_max)

        return res