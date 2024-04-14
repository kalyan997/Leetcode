class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        curr_permutation = []
        my_map = defaultdict(int)
        for num in nums:
            my_map[num] += 1
            
        def backtrack():
            if len(curr_permutation)==len(nums):
                permutations.append(curr_permutation.copy())
                return
            for key,value in my_map.items():
                if key in my_map and my_map[key]!=0:
                    curr_permutation.append(key)
                    my_map[key] -= 1
                    backtrack()
                    curr_permutation.pop()
                    my_map[key] += 1
            return
            
        backtrack()
        return permutations