# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        avg_of_levels = []
        my_q = deque()

        my_q.append(root)

        while my_q:
            level_size = len(my_q)
            level_sum = 0
            for i in range(level_size):
                curr = my_q.popleft()
                level_sum += curr.val
                if curr.left is not None:
                    my_q.append(curr.left)
                if curr.right is not None:
                    my_q.append(curr.right)
            avg_of_levels.append(level_sum/level_size)

        return avg_of_levels