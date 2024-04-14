class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        print(g)
        g.sort(reverse=True)
        s.sort(reverse =True)
        
        g_ind, s_ind = 0,0
        res = 0
        

        while g_ind<len(g) and s_ind<len(s):
            if s[s_ind]>=g[g_ind]:
                g_ind += 1
                s_ind += 1
                res +=1
            else:
                g_ind += 1
        
        return res    