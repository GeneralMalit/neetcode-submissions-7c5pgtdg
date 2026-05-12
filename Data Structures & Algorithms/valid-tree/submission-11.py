from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        q = deque([0])
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        visited.add(0)

        while q:
            curr = q.popleft()
            for nei in adj[curr]:
                if nei not in visited:
                    q.append(nei)
                    visited.add(nei)

        return len(visited) == n