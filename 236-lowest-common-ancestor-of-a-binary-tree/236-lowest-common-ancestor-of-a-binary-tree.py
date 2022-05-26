# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lo_ancestor = None
        
        def find_lo_ancestor(root):
            if root is None:
                return 0
            nonlocal lo_ancestor
            if not lo_ancestor:
                # check if current is p or q
                current = 0
                if root == p or root == q:
                    current = 1
                left = find_lo_ancestor(root.left)
                right = find_lo_ancestor(root.right)
                
                found_ancestors = left + right + current
                if found_ancestors == 2:
                    lo_ancestor = root
                else:
                    return found_ancestors
            return 0
            
            
            
        find_lo_ancestor(root)
        return lo_ancestor