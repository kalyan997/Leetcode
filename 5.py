class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        num_even_palindromes = 0
        num_odd_palindromes = 0
        longest_palindrome = ""
        final_left, final_right = 0, 0
        for i in range(0, n):
            left, right = i, i

            while left >=0 and right < n:
                if s[left] != s[right]:
                    break
                if (right-left+1) > (final_right-final_left+1):
                    final_left, final_right = left, right
                num_even_palindromes += 1
                left, right = left-1, right+1

        for i in range(0, n-1):
            left, right = i, i+1

            while left >=0 and right < n:
                if s[left] != s[right]:
                    break
                if (right-left+1) > (final_right-final_left+1):
                    final_left, final_right = left, right
                num_odd_palindromes += 1
                left, right = left-1, right+1


        num_palindromes = num_even_palindromes + num_odd_palindromes
        return s[final_left:final_right+1]