# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_traversal = []
        if root is None:
            return level_order_traversal

        my_q = deque()
        my_q.append(root)
        #my_q.append(None)
        curr_level = []
        level_num = 0
        while my_q:
            curr_size = len(my_q)
            curr_level = []
            level_num += 1
            for i in range(curr_size):
                curr_node = my_q.popleft()
                curr_level.append(curr_node.val)
                if curr_node.left:
                    my_q.append(curr_node.left)
                if curr_node.right:
                    my_q.append(curr_node.right)
            if level_num%2==0:
                level_order_traversal.append(curr_level[::-1])
            else:
                level_order_traversal.append(curr_level)
        return level_order_traversal