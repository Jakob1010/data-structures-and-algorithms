# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True
        
        def checkHeight(root):
            nonlocal isBalanced
            if root is None or not isBalanced:
                return 0
            

            
            left = checkHeight(root.left)
            right = checkHeight(root.right)

            if abs(left-right) > 1:
                isBalanced = False


            return max(left+1,right+1)
        
        checkHeight(root)
        return isBalanced
        
        