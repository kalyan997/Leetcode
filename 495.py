class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        curr_end = -1
        total_time = 0
        
        for curr_time in timeSeries:
            
            if curr_time > curr_end:
                total_time += duration
                #curr_end = curr_time + duration - 1
            else:
                rem_dur = duration-(curr_end-curr_time+1)
                total_time += rem_dur
            curr_end = curr_time + duration - 1
            #print(curr_end, total_time)
        return total_time