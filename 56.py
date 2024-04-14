class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        merged_intervals = []
        curr_end = -1

        for i,interval in enumerate(intervals):
            if curr_end < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(interval[1],merged_intervals[-1][1])
            curr_end = merged_intervals[-1][1]
        return merged_intervals