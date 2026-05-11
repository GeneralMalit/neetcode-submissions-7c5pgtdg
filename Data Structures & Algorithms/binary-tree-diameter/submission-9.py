# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        
        def dfs(root):
                
                if not root:
                        return 0

                print(f"root =  {root.val}")
                left = dfs(root.left)
                right = dfs(root.right)
                self.d = max(self.d, left + right)
                print(f"returns 1 + {left}, {right} for {root.val}")
                return 1 + max(left, right)
        dfs(root)
        return self.d