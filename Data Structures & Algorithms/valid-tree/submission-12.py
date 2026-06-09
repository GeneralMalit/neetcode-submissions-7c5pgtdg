from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 != n:
            return False
        
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        q = deque([0])
        visited = set()
        visited.add(0)

        while q:
            curr = q.popleft()
            for nei in adj_list[curr]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)

        return len(visited) == n
        