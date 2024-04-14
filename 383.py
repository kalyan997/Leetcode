class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(magazine) < len(ransomNote):
            return False
        
        magazine_map = defaultdict(int)
        ransomNote_map = defaultdict(int)
        
        for c in magazine:
            magazine_map[c] += 1
        
        for c in ransomNote:
            ransomNote_map[c] += 1
            
            if magazine_map[c] < ransomNote_map[c]:
                return False
           
        return True
        