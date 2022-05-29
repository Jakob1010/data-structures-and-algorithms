# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        
        def get_max_diameter(root):
            if not root:
                return 0
            
            nonlocal max_diameter
            left = get_max_diameter(root.left)
            right = get_max_diameter(root.right)
            max_diameter = max(max_diameter, left+right)
            
            return 1+max(left,right)
        
        get_max_diameter(root)
        return max_diameter
        
        
        
        