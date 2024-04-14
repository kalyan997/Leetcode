class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        pattern_map = defaultdict(int)
        s_map = defaultdict(int)
        
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            
            if pattern_map[pattern[i]] != s_map[words[i]]:
                return False
            pattern_map[pattern[i]] = i+1
            s_map[words[i]] = i+1
        
        return True