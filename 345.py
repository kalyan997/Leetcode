class Solution:
    def reverseVowels(self, s: str) -> str:
        
        left, right = 0, len(s)-1
        chars = list(s)
        vowels = {'a','e','i','o','u','A','E','I','O','U'}
        
        while left < right:
            if chars[left] in vowels and chars[right] in vowels:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
            if left< len(s) and chars[left] not in vowels:
                left += 1
                
            if right>0 and chars[right] not in vowels:
                right -= 1
        res ="".join(i for i in chars)
        return res