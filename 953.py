class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        my_map = defaultdict(int)
        curr = 1
        for c in order:
            my_map[c] = curr
            curr = curr+1
        n = len(words)
        for i in range(n-1):
            curr_word = words[i]
            next_word = words[i+1]
            
            min_len = min(len(curr_word),len(next_word))

            for j in range(min_len):
                curr_c = curr_word[j]
                next_c = next_word[j]
                if curr_c != next_c and my_map[curr_c]<my_map[next_c]:
                    break
                if curr_c != next_c and my_map[curr_c]>my_map[next_c]:
                    return False
                if j==min_len-1 and len(curr_word)>len(next_word):
                    return False
                
        return True
                