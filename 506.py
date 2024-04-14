class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        my_map = defaultdict(int)
        
        for i, num in enumerate(score):
            my_map[num] = i
            
        res = ["1"]*len(score)
        curr = len(score)-1
        
        score.sort()
        
        for num in score:
            curr_ind = my_map[num]
            if curr == 0:
                res[curr_ind ] = "Gold Medal"
            elif curr == 1:
                res[curr_ind] = "Silver Medal"
            elif curr == 2:
                res[curr_ind] = "Bronze Medal"
            else:
                res[curr_ind] = str(curr+1)
            curr -= 1
        return res