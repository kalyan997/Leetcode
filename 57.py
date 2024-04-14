class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        res = []
        intervals.append(newInterval)
        intervals.sort()
        
        curr_end = -1
        
        for interval in intervals:
            if curr_end < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(curr_end, interval[1])
            curr_end = res[-1][1]
            
        return res