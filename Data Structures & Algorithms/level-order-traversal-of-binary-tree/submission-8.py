# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stk = [root]
        res = []
        while stk:
            level = []
            next_level = []
            for node in stk:
                level.append(node.val)
                if node and node.left:
                    next_level.append(node.left)
                if node and node.right:
                    next_level.append(node.right)
            
            res.append(level[:])
            stk = next_level
        return res
