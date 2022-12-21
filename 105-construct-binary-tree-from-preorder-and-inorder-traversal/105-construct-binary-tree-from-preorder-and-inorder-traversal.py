# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_idx = {}
        preorder_idx = 0
        for i, num in enumerate(inorder):
            inorder_idx[num] = i
            
        def build_tree(left,right):
            if left > right:
                return 
            
            nonlocal preorder_idx
            root = TreeNode(preorder[preorder_idx])
            iorder_idx = inorder_idx[root.val]
            preorder_idx += 1
            root.left = build_tree(left,iorder_idx-1)
            root.right = build_tree(iorder_idx+1,right)
            return root
            
            
        return build_tree(0,len(inorder)-1)