# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum = -float('inf')
        
        def postorder(root):
            if root is None:
                return 0
            nonlocal maxPathSum
            
            left = postorder(root.left)
            right = postorder(root.right)
            
            root_val = root.val
            root.val = max(root.val,root.val + left,root.val + right)
            maxPathSum = max(root.val,maxPathSum,root_val+left+right)
            
            return root.val
            
            
            
        
        postorder(root)
        return maxPathSum