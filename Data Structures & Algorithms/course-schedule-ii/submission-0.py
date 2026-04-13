from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        res = []
        in_degree = numCourses * [0]
        q = deque()
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1

        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)
            
        while q:
            course = q.popleft()
            res.append(course)
            for prereq in adj_list[course]:
                in_degree[prereq] -= 1
                if in_degree[prereq] == 0:
                    q.append(prereq)
            
        return res if len(res) == numCourses else []