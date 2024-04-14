class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_states = []
        terminal_states = []
        visited = set()
        for i in range(len(graph)):
            if len(graph[i])==0:
                terminal_states.append(i)

        #reverse edges
        adjList = defaultdict(list)
        indegree = [0]*(len(graph))

        for i in range(len(graph)):
            for neigh in graph[i]:
                adjList[neigh].append(i)
                indegree[i] += 1

        my_q = deque()

        for i in range(len(graph)):
            if indegree[i]==0:
                my_q.append(i)
                

        while my_q:
            curr = my_q.popleft()
            safe_states.append(curr)
            for neigh in adjList[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    my_q.append(neigh)

        return sorted(safe_states)