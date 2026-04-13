# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def isSameTree(r, sr):
            if not r and not sr:
                return True
            
            if not r or not sr or r.val != sr.val:
                return False

            return isSameTree(r.left, sr.left) and isSameTree(r.right, sr.right)
        
        if isSameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

