class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = defaultdict(set)

        for time in times:
            curr_u = time[0]
            curr_v = time[1]
            dist = time[2]

            adjList[curr_u].add((curr_v,dist))

        
        visited = set()
        res = -1
        min_heap = []
        heapq.heappush(min_heap,[0,k])

        while len(visited)<n and len(min_heap)>0:
            print(min_heap)
            curr_dist, curr_node = heapq.heappop(min_heap)
            print(curr_dist)
            if curr_node in visited:
                continue
            res = max(res,curr_dist)
            visited.add(curr_node)
            for neigh in adjList[curr_node]:
                print(neigh)
                if curr_dist+neigh[1]<neigh[1]:
                    heapq.heappush(min_heap,[curr_dist+neigh[1],neigh[0]])
                else:
                    heapq.heappush(min_heap,[neigh[1],neigh[0]])
            


        
        return res if len(visited) == n else -1
        