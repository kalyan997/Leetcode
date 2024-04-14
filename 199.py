# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root is None:
            return res

        my_q = deque()
        my_q.append(root)
        while my_q:
            curr_size = len(my_q)

            for i in range(curr_size):
                curr_node = my_q.popleft()
                if i==curr_size-1:
                    res.append(curr_node.val)
                if curr_node.left != None:
                    my_q.append(curr_node.left)
                if curr_node.right != None:
                    my_q.append(curr_node.right)
                
        return res