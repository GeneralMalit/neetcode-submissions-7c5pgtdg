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

        def build(l, r):
            if l > r:
                return None
            
            preorder_val = preorder[self.preorder_idx]
            self.preorder_idx += 1
            root = TreeNode(preorder_val)

            inorder_idx = inorder_dict[preorder_val]
            root.left = build(l, inorder_idx - 1)
            root.right = build(inorder_idx + 1, r)

            return root
        return build(0, len(inorder) - 1)