class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        set1 = set()
        set2 = set()
        visited = set()
        num_comp = 0
        
        my_q = deque()
        # set1.add(0)
        # my_q.append(0)
        for node in range(len(graph)):
            if node not in visited:
                my_q.append(node)
                set1.add(node)
                visited.add(node)
            while my_q:
                curr = my_q.popleft()
                visited.add(curr)
                #print(curr)
                for j in graph[curr]:
                    if curr in set1 and j in set1:
                        return False
                    if curr in set2 and j in set2:
                        return False
                    if curr in set1:
                        if j not in set2:
                            my_q.append(j)
                            set2.add(j)
                    if curr in set2:
                        if j not in set1:
                            my_q.append(j)
                            set1.add(j)
        print(set1,set2)
        
        return True