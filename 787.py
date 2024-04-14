class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        cost = [float("inf")]*n
        cost[src] = 0
        for i in range(k+1):
            temp_cost = cost.copy()
            for flight in flights:
                curr_u, curr_v  = flight[0], flight[1]
                curr_price = flight[2]
                if temp_cost[curr_u] == float("inf"):
                    continue
                if cost[curr_u]+curr_price < temp_cost[curr_v]:
                    temp_cost[curr_v] = cost[curr_u]+curr_price
            cost = temp_cost
        return cost[dst] if cost[dst]!=float("inf") else -1