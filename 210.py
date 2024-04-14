class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_isprereq_of = [[] for _ in range(numCourses)]
        indegree = [0]*numCourses
        topological_sort = []
        for prereq in prerequisites:
            course_isprereq_of[prereq[1]].append(prereq[0])
            indegree[prereq[0]] += 1
        print(indegree)
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

        return topological_sort if len(topological_sort)==numCourses else []