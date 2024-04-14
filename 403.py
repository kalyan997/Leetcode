class Solution:
    def canCross(self, stones: List[int]) -> bool:
        my_map = defaultdict(list)

        curr_pos, curr_step = stones[0], 1

        if curr_pos+curr_step != stones[1]:
            return False
        
        curr_pos = stones[1]

        my_map[stones[1]].append(1)

        for i in range(1, len(stones)):
            curr_pos = stones[i]
            for prev_jump in my_map[curr_pos]:
                if prev_jump>0:
                    my_map[curr_pos+prev_jump].append(prev_jump)
                if prev_jump+1>0:
                    my_map[curr_pos+prev_jump+1].append(prev_jump+1)
                if prev_jump-1>0:
                    my_map[curr_pos+prev_jump-1].append(prev_jump-1)

        return len(my_map[stones[-1]]) != 0