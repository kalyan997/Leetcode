class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        position_time = []

        for i in range(n):
            time = (target - position[i]) / speed[i]
            position_time.append((position[i], time))

        position_time.sort()
        print(position_time)
        num_fleets = 0
        max_time = 0.0

        for i in range(n - 1, -1, -1):
            time = position_time[i][1]
            if time > max_time:
                max_time = time
                num_fleets += 1

        return num_fleets
