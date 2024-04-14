class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letter_combinations = []
        curr_comb = []
        if len(digits)==0:
            return []

        my_map = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        
        def backtrack(i):
            if len(curr_comb)==len(digits):
                letter_combinations.append("".join(curr_comb))
                return
            curr_mapping = my_map[digits[i]]
            for c in curr_mapping:
                curr_comb.append(c)
                backtrack(i+1)
                curr_comb.pop()
            return

        backtrack(0)
        return letter_combinations