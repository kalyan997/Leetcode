class Solution:
    def checkRecord(self, s: str) -> bool:
        
        A_count = 0
        L_streak = 0
        for c in s:
            if c == 'A':
                A_count += 1
            if c == 'L':
                L_streak += 1
            else:
                L_streak = 0
            if L_streak >= 3 or A_count>=2:
                return False
        return True