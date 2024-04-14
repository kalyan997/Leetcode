"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        oldToNew = {}
        my_q = deque()

        copy_node = Node(node.val,[])
        oldToNew[node] = copy_node
        my_q.append(node)
        
        while my_q:
            curr_node = my_q.popleft()
            for neighbor in curr_node.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val,[])
                    my_q.append(neighbor)
                oldToNew[curr_node].neighbors.append(oldToNew[neighbor]) 

        return copy_node