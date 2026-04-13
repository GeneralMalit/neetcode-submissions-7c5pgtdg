# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.curr_max = float('-inf')
        def func(node):
            if not node:
                return 0
            
            left = max(func(node.left), 0)
            right = max(func(node.right), 0)

            self.curr_max = max(self.curr_max, left + right + node.val)
            return node.val + max(left, right)

        func(root)
        return self.curr_max
