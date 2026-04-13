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
        res = []

        level = [root]
        while level:
            next_level = []
            this_level = []
            for i in level:
                this_level.append(i.val)
                if i.left: next_level.append(i.left)
                if i.right: next_level.append(i.right)

            res.append(this_level)
            level = next_level
        return res