# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        bst = []
        
        def BST_to_list(root,bst):
            if root is None:
                return 
            
            BST_to_list(root.left,bst)
            bst.append(root.val)
            BST_to_list(root.right,bst)
            
            return root
            
        
        BST_to_list(root,bst)
        for i in range(1,len(bst)):
            if bst[i] <= bst[i-1]:
                return False
        return True