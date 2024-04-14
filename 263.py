class Solution:
    def isUgly(self, n: int) -> bool:
        
        accepted_primes = [2, 3, 5]
        if n == 0:
            return False
        for curr_prime in accepted_primes:
            while n%curr_prime == 0:
                n = n//curr_prime
            
        return n == 1