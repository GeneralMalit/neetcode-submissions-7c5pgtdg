"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_new = {}
        def bfs(node):
            if node in old_new:
                return old_new[node]
            
            copynode = Node(node.val)
            old_new[node] = copynode

            for neighbor in node.neighbors:
                copynode.neighbors.append(bfs(neighbor))
            
            return copynode
        return bfs(node) if node else None