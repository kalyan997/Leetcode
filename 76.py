class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        t_map = collections.Counter(t)
        N = len(s)
        
        left = 0
        best_start = None
        best = N+1
        
        window_map = collections.Counter()
        
        for right in range(N):
            window_map[s[right]] += 1
            
            if all(window_map[i] >= t_map[i] for i in t_map.keys()):
                while window_map[s[left]] > t_map[s[left]]:
                    window_map[s[left]] -= 1
                    left += 1
                    
                if right-left+1 < best:
                    best = right-left+1
                    best_start = left
        if best_start is None:
            return ""
        return s[best_start:best_start+best]
                    
            
        