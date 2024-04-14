class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        neighbors = defaultdict(set)
        if source == target:
            return 0
        for i in range(len(routes)):
            for j in range(i+1,len(routes)):
                curr_node = routes[i]
                next_node = routes[j]
                for curr_city in curr_node:
                    if curr_city in next_node:
                        neighbors[tuple(curr_node)].add(tuple(next_node))
                        neighbors[tuple(next_node)].add(tuple(curr_node))
                
                    
        visited = set()
        my_q = deque()
        for route in routes:
            if source in route:
                my_q.append(tuple(route))
                visited.add(tuple(route))

        curr_level = 0
        while my_q:
            curr_len = len(my_q)
            curr_level += 1
            for i in range(len(my_q)):
                curr = my_q.popleft()
                if target in curr:
                    return curr_level
                for neighbor in neighbors[curr]:
                    if neighbor not in visited:
                        my_q.append(neighbor)
                        visited.add(neighbor)
        
        return -1