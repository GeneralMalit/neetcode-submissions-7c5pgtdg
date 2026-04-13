from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq_list = defaultdict(list)
        for course, prereq in prerequisites:
            prereq_list[course].append(prereq)
        
        visited = set()

        def hasCycle(node):
            if node in visited:
                return True

            if not prereq_list[node]:
                return False

            visited.add(node)

            for prereq in prereq_list[node]:
                if hasCycle(prereq):
                    return True
            
            visited.remove(node)
            prereq_list[node] = []

            return False

        for i in range(numCourses):
            if hasCycle(i):
                return False
        return True
