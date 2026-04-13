class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]
        def union(u, v):
            root1 = find(u)
            root2 = find(v)
            if root1 != root2:
                parent[root2] = root1
                return 1
            return 0
        
        count = n
        for u, v in edges:
            count -= union(u, v)
        return count