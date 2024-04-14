class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low = 1
        high = max(piles)

        def koko_can_finish(curr_speed):
            piles_copy = piles.copy()
            if len(piles)==0:
                return True
            curr_h = 0
            for i in range(len(piles_copy)):
                curr_h += math.ceil(piles_copy[i]/curr_speed)
            return curr_h<=h


        while low < high:
            mid = low + (high-low)//2
            #print(mid)
            if not koko_can_finish(mid):
                low = mid + 1
            else:
                high = mid
        return high