# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_idx = 0
        inorder_dict = {val:idx for idx, val in enumerate(inorder)}

        def dfs(l, r):
            if l > r:
                return
            node_val = preorder[self.preorder_idx]
            node = TreeNode(node_val)
            self.preorder_idx += 1
            
            inorder_idx = inorder_dict[node_val]
            node.left = dfs(l, inorder_idx - 1)
            node.right = dfs(inorder_idx + 1, r)
            
            return node
        
        return dfs(0, len(inorder) - 1)