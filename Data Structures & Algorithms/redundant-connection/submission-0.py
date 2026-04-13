class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = list(range(len(edges) + 1))
        size = [1] * (len(edges) + 1)

        def find(i):
            if par[i] != i:
                par[i] = find(par[i])
            return par[i]
        def union(u, v):
            p1, p2 = find(u), find(v)
            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                par[p2] = p1
                size[p1] += size[p2]
            else:
                par[p1] = p2
                size[p2] += size[p1]
    
            return True
    

        for u, v in edges:
            if not union(u, v):
                return [u, v]