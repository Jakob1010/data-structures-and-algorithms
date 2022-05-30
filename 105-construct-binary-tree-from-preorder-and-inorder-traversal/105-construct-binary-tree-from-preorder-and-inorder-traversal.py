# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_dict = {}
        preorder_idx = 0
        
        for i, num in enumerate(inorder):
            inorder_dict[num] = i
        
        def build_tree(left, right):
            nonlocal preorder_idx
            
            if left > right:
                return None


            root = TreeNode(preorder[preorder_idx])
            root_val = preorder[preorder_idx]
            preorder_idx += 1

            root.left = build_tree(left, inorder_dict[root_val]-1)
            root.right = build_tree(inorder_dict[root_val]+1, right)


            return root
        
        return build_tree(0, len(preorder)-1)
        
        