class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        
        words = sentence.split()
        
        vowels = {'a','e','i','o','u',"A","E","I","O","U"}
        
        curr_suffix = ""
        res = ""
        for word in words:
            curr_suffix += "a"
            if word[0] in vowels:
                word += "ma"
            else:
                word = word[1:]+word[0]+"ma"
            word += curr_suffix
            res = res +" "+ word
            
        res =res.strip()
        
        return res