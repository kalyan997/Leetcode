class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        curr_index = 0
        res = ""
        while curr_index<len(s):
            curr_word = ""
            while s[curr_index] != " ":
                curr_word += s[curr_index]
                if curr_index==len(s)-1:
                    break
                curr_index+=1
            words.append(curr_word)
            curr_index+=1
        for i in range(len(words)):
            words[i]=words[i][::-1]
        res= " ".join(words)
        return res