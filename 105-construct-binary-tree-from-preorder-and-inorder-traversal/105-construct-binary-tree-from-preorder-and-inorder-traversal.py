# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorder_idx = 0
        inorder_map = {}
        
        for i, num in enumerate(inorder):
            inorder_map[num] = i
            
        def build_tree(left,right):
            nonlocal preorder_idx
            if left > right or preorder_idx >= len(preorder):
                return None
            
            root = TreeNode(preorder[preorder_idx])
            root_val = root.val
            preorder_idx += 1
            
            root.left = build_tree(left,inorder_map[root_val]-1)
            root.right = build_tree(inorder_map[root_val]+1,right)
            
            return root
            
            
        return build_tree(0,len(inorder)-1)