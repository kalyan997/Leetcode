class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [0]*n
        size = [0]*n
        
        def make(i):
            parent[i]=i
            size[i]=i

        def find(i):
            if parent[i]!=i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(a,b):
            a = find(a)
            b = find(b)
            if a!=b:
                if size[a]<size[b]:
                    parent[a] = b
                    size[b]+=size[a]
                else:
                    parent[b] = a
                    size[a]+=size[b]
            return

        for i in range(n):
            make(i)

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1:
                    if(find(i)!=find(j)):
                        union(i,j)
        
        num_provinces = 0
        for i in range(n):
            if parent[i]==i:
                num_provinces+=1

        return num_provinces