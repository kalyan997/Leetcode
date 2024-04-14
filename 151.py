class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len( words)):
            words[i] = words[i][::-1]
        strn = ''
        for i in range(len(words)):
            strn = strn + words[i]+ ' '
        strn = strn[:-1]
        strn = strn[::-1]
        strn = strn.strip()
        return strn
            