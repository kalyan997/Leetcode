class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n= len(intervals)
        intervals.sort()

        prev_end = intervals[0][1]
        res = 0

        for interval in intervals[1:]:
            if interval[0]>=prev_end:
                prev_end = interval[1]
            else:
                res += 1
                prev_end = min(prev_end,interval[1])

        return res

