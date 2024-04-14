class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        res = []
        final_word2_dict = defaultdict(int)
        
        for word in words2:
            word_dict = Counter(word)
            for key, val in word_dict.items():
                if final_word2_dict[key] < val:
                    final_word2_dict[key] = val
        
        #print(final_word2_dict)
        for word1 in words1:
            word1_dict = Counter(word1)
            is_subset = True
            for key, val in final_word2_dict.items():
                if word1_dict[key] < final_word2_dict[key]:
                    is_subset = False
                    break
            if is_subset:
                res.append(word1)
        return res