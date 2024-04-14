class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res = ""
        
        curr_index = len(s)-1
        groups = []
        while curr_index>=0:
            curr_group_len = 0
            curr_group = ""
            while curr_group_len < k and curr_index >= 0:
                if s[curr_index] != '-':
                    c = s[curr_index]
                    if ord(c) >= ord('a') and ord(c)<=ord('z'):
                        c = chr(ord('A')+ord(c)-ord('a'))
                    curr_group = c + curr_group
                    curr_group_len += 1
                curr_index -= 1
            if curr_index != -1:
                curr_group = "-" + curr_group
            res = curr_group+res
            
        res = res.lstrip('-')
        return res