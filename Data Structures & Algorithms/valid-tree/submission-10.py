from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not len(edges) == n - 1:
            return False
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        visited.add(0)
        q = [0]

        while q:
            node = q.pop()
            for nei in adj[node]:
                print(f"nei is {nei}")
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        
        return len(visited) == n

