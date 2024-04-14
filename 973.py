class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def SquaredDistFromOrg(x,y):
            return x**2 + y**2
        max_heap = []
        res = []
        for point in points:
            dist_point = []
            dist = SquaredDistFromOrg(point[0],point[1])
            #print(dist)
            dist_point.append(-dist)
            dist_point.append(point)
            heapq.heappush(max_heap,dist_point)
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        while max_heap:
            curr = heapq.heappop(max_heap)
            print(curr)
            res.append(curr[1])
        return res
