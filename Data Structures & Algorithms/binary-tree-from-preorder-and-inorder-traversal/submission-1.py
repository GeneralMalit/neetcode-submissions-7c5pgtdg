# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.in_map = {val: idx for idx, val in enumerate(inorder)}
        self.preorder_idx = 0

        def build(l, r):
            if l > r:
                return None

            root_val = preorder[self.preorder_idx]
            root = TreeNode(root_val)
            self.preorder_idx += 1

            inorder_idx = self.in_map[root_val]
            root.left = build(l, inorder_idx - 1)
            root.right = build(inorder_idx + 1, r)

            return root
        
        return build(0, len(self.in_map) - 1)