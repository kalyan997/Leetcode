class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        #adjList = defaultdict(list)
        n = len(graph)
        paths = []
        curr_path = []
        
        def dfs(i):
            curr_path.append(i)
            if i==n-1:
                paths.append(curr_path.copy())
            for neighbor in graph[i]:
                dfs(neighbor)
            curr_path.pop()
        
        dfs(0)
        
        return paths