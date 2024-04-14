class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        res = [[0]*i for i in range(1,102)]

        res[0][0] = poured

        for r in range(100):
            for c in range(r+1):
                rem = (res[r][c]-1.0)/2.0
                
                if rem > 0:
                    res[r][c] = 1
                    res[r+1][c] += rem
                    res[r+1][c+1] += rem
        print(res)
        return res[query_row][query_glass]
        #min(1,res[query_row][query_glass])