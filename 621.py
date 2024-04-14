class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        my_map = {}
        for c in tasks:
            my_map[c] = my_map.get(c,0)+1
        
        max_freq = 0
        for key,value in my_map.items():
            max_freq = max(max_freq, value)
        n_max = 0
        for key,value in my_map.items():
            if max_freq == value:
                n_max += 1
                
        return max(len(tasks),(n+1)*(max_freq-1)+n_max)