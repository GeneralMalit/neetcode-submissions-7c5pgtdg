# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, NewType0, left=None, right=None):
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
            next_floor = []
            this_floor = []
            for i in level:
                if i.left: next_floor.append(i.left)
                if i.right: next_floor.append(i.right)
                this_floor.append(i.val)
            
            res.append(this_floor)
            level = next_floor
        return res