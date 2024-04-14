class Solution:
    def frequencySort(self, s: str) -> str:
        
        char_freq = defaultdict(int)
        
        for c in s:
            char_freq[c] += 1
        
        count_chars = defaultdict(list)
        for key, val in char_freq.items():
            count_chars[val].append(key)
            
        res = []
        for i in range(len(s),-1,-1):
            for c in count_chars[i]:
                res.append(c*i)
        return "".join(res)