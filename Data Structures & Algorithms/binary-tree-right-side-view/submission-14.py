# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        level = [root]
        while level:
            res.append(level[-1].val)
            next_level = []
            for i in level:
                if i.left: next_level.append(i.left)
                if i.right: next_level.append(i.right)
            level = next_level
        return res