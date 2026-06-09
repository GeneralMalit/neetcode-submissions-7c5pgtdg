from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        visited = set()

        def hasCycle(course):
            if course in visited:
                return True
            
            if not adj_list[course]:
                return False
            
            visited.add(course)
            for prereq in adj_list[course]:
                if hasCycle(prereq):
                    return True
            visited.remove(course)
            adj_list[course] = []                
            
            return False


        for i in range(numCourses):
            if hasCycle(i):
                return False
        
        return True