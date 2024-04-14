class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:

        visited = set()
        my_q = deque()
        my_q.append(0)
        visited.add(0)

        edges = [jug1Capacity, jug2Capacity, -jug1Capacity, -jug2Capacity]

        if targetCapacity>jug1Capacity+jug2Capacity or targetCapacity<0:
            return False
        
        while my_q:
            curr = my_q.popleft()
            for edge in edges:
                if curr+edge>0 and curr+edge <= jug1Capacity+jug2Capacity and curr+edge not in visited:
                    my_q.append(curr+edge)
                    visited.add(curr+edge)
                
        return targetCapacity in visited