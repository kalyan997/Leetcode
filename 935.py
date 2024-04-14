class Solution:
    def knightDialer(self, n: int) -> int:
        neighbors = {0: {4, 6}, 1: {8, 6}, 2: {7, 9}, 3: {4, 8},
              4: {0, 3, 9}, 5: {}, 6: {0, 1, 7}, 7: {2, 6},
              8: {1, 3}, 9: {2, 4}}

        prev = [1]*10
        MOD = 10**9 + 7
        
        for i in range(2,n+1):
            curr = [0]*10
            for j in range(10):
                for k in neighbors[j]:
                    curr[k] += prev[j]
            prev = curr

    
        res = 0
        for i in range(10):
            res = (res+prev[i])%MOD


        return res