# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalmax = float('-inf')

        def traverse(node):
            if not node:
                return 0

            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)

            curr_path = node.val + left + right
            self.globalmax = max(self.globalmax, curr_path)

            return node.val + max(left, right)
        traverse(root)
        return self.globalmax