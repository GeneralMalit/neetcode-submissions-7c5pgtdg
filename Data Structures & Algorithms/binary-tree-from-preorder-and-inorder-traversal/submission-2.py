# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preorder_index = 0
        inorder_dict = {val:idx for idx, val in enumerate(inorder)}
        def build(l, r):
            if l > r:
                return None

            root_val = preorder[self.preorder_index]
            root = TreeNode(root_val)
            midpoint = inorder_dict[root_val]
            self.preorder_index += 1

            root.left = build(l, midpoint - 1)
            root.right = build(midpoint + 1, r)

            return root


        return build(0, len(inorder_dict) - 1)
