class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        min_diff = 10**7+1
        res = [0]*2
        
        mid = math.ceil(sqrt(area))
        for L in range(mid,area+1):
            if area%L == 0:
                W = area//L
                return [L,W]
                
        return res
                