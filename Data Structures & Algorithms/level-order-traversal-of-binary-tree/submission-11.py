# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        curr = deque([root])

        while curr:
            next_level = []
            ans = []
            for i in range(len(curr)):
                node = curr.popleft()
                ans.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            curr = deque(next_level)
            res.append(ans)
        return res


