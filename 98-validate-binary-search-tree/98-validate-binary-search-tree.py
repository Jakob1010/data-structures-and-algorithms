# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        isValid = True
        def validate(root,last):
            nonlocal isValid
            if isValid and root:
                last = validate(root.left,last)
                if root.val <= last:
                    isValid = False
                else:
                    last = root.val
                last = validate(root.right,last)
                
            return last
                
            
            
        validate(root,-float('inf'))
        return isValid