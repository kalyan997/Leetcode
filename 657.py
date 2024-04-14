class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ups = 0
        downs =0
        lefts =0
        rights =0
        for i in moves:
            if i == 'U':
                ups += 1
            elif i == 'D':
                downs += 1
            elif i == 'L':
                lefts += 1
            else:
                rights += 1
        if ups == downs and lefts == rights:
            return 1
        else:
            return 0
        
                
        