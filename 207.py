class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_isprereq_of = defaultdict(list)
        indegree = [0]*numCourses
        topological_sort = []
        for prereq in prerequisites:
            course_isprereq_of[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1

        my_q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                my_q.append(i)

        while my_q:
            curr_node = my_q.popleft()
            topological_sort.append(curr_node)
            if course_isprereq_of[curr_node]:
                for neighbor in course_isprereq_of[curr_node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor]==0:
                        my_q.append(neighbor)

        return len(topological_sort)==numCourses