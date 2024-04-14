class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n= len(nums)
        my_map = {}
        for i in range(n):
            if nums[i] not in my_map:
                my_map[nums[i]] = 1
            else: 
                my_map[nums[i]] += 1

        print(my_map)
        sorted_map = sorted(my_map.items(), key=lambda item: item[1],reverse = True)
        res = []
        for i in range(k):
            res.append(sorted_map[i][0])
        return res