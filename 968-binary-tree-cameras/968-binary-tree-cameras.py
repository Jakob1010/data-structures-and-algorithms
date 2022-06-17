# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        self.cnt = 0
        
        def post_ord(root):
            if root is None:
                return
            
            post_ord(root.left)
            post_ord(root.right)
            
            if root.left and root.left.val == 1:
                root.val = 2
            if root.right and root.right.val == 1:
                root.val = 2
            
            if root.left and root.left.val == 0:
                root.val = 1
                self.cnt += 1
            elif root.right and root.right.val == 0:
                root.val = 1
                self.cnt += 1
    
            
        post_ord(root)
        if root.val == 0:
            self.cnt += 1
        return self.cnt
        