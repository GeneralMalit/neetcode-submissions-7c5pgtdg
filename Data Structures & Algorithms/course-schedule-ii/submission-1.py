from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        q = deque()
        in_degree = [0] * numCourses
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)
        res = []
        while q:
            subj = q.popleft()
            res.append(subj)
            for prereq in adj_list[subj]:
                in_degree[prereq] -= 1
                if in_degree[prereq] == 0:
                    q.append(prereq)
        
        return res if len(res) == numCourses else []