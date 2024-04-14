class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_map = defaultdict(list)
        
        for curr in strs:
            key = ''.join(x for x in sorted(curr))
            
            my_map[key].append(curr)
        
        return list(my_map.values())