from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) + 1 != n:
            return False
        adj_list = defaultdict(list)
        q = deque([0])
        visited = set()
        visited.add(0)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        while q:
            curr = q.popleft()
            for nei in adj_list[curr]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return len(visited) == n