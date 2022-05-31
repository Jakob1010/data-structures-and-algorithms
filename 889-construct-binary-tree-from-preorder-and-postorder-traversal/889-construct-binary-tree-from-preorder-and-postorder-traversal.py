# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        pre_idx, post_idx = 0, 0
        
        def build_tree():
            nonlocal pre_idx
            nonlocal post_idx
            
            root = TreeNode(preorder[pre_idx])
            pre_idx += 1
            if root.val != postorder[post_idx]:
                root.left = build_tree()
            if root.val != postorder[post_idx]:
                root.right = build_tree()
            
            if postorder[post_idx] == root.val:
                post_idx += 1
                
            return root
        
        return build_tree()
            