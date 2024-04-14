class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [0]* (int)(n+1)
        size = [0]* (int)(n+1)
        def make(i):
            parent[i] = i
            size[i] = 1

        def find(i):
            if parent[i]!= i:
                parent[i] = find(parent[i])
            return parent[i]
  
        def union(a, b):
            a = find(a)
            b = find(b)
            if(a!=b):
                if size[a]<size[b]:
                    parent[a]=b
                    size[b]+=size[a]
                else:
                    parent[b]=a
                    size[a]+=size[b]
            return
        for i in range(n):
            make(i)
        res = []
        for edge in edges:
            if find(edge[0])!=find(edge[1]):
                union(edge[0],edge[1])
            else:
                res.append(edge)
        return res[-1]