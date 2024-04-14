class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        
        points.sort()
        res = len(points)
        prev =points[0]
        res = 1
        
        for i in range(1,len(points)):
            curr = points[i]
            
            if curr[0] <= prev[1]:
                #res -= 1
                prev = [curr[0],min(curr[1], prev[1])]
            else:
                res += 1
                prev = curr
                
            
        return res