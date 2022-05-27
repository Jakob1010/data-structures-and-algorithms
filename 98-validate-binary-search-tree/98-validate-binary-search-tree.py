# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last = -float('inf')
        
        def BST_to_list(root):
            nonlocal last
            if not root:
                return True
            
            
            if not BST_to_list(root.left) or root.val <= last:
                return False
            last = root.val
            return BST_to_list(root.right)
            

        return BST_to_list(root)