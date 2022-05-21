# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSymmetricRec(leftSub,rightSub):
            if not leftSub and not rightSub:
                return True
            elif not leftSub or not rightSub or (leftSub.val != rightSub.val):
                return False
            
            return isSymmetricRec(leftSub.left,rightSub.right) and isSymmetricRec(leftSub.right,rightSub.left)
        
        return isSymmetricRec(root.left,root.right)