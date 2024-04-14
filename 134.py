class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)

        curr_tank = 0
        total_tank = 0
        starting_point = 0
        for i in range(n):
            
            curr_tank += gas[i] - cost[i]
            total_tank += gas[i] - cost[i]
            if curr_tank < 0:
                starting_point = i+1
                curr_tank = 0
            
        return starting_point if total_tank>=0 else -1