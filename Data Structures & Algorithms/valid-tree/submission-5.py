from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)
        
        q = deque()
        visited = set()
        q.append(0)
        visited.add(0)

        while q:
            node = q.popleft()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)

        return len(visited) == n