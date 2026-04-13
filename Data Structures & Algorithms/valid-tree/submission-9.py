from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        edge_list = defaultdict(list)
        for u, v in edges:
            edge_list[u].append(v)
            edge_list[v].append(u)

        visited = set()
        q = [0]
        visited.add(0)

        while q:
            node = q.pop()
            for neighbor in edge_list[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        
        return len(visited) == n