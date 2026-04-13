# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append('N')
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        out = ",".join(res)
        print(f"{out}")
        return out
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        d = iter(data.split(','))
        def build():
            try:
                value = next(d)
            except StopIteration:
                return
            
            if value == 'N':
                return
            
            node = TreeNode(int(value))
            node.left = build()
            node.right = build()

            return node
        return build()


