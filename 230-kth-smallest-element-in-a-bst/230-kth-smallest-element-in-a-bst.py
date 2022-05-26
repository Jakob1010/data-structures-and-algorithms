# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    

        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        kth_small_node = None
    
        def find_kth_smallest(root):
            if root is None:
                return
            
            nonlocal kth_small_node
            nonlocal k
            
            if not kth_small_node:                
                find_kth_smallest(root.left)
                k -= 1        
                if k == 0:
                    kth_small_node = root.val   
                find_kth_smallest(root.right)
     
                return 
            
            return
          
        find_kth_smallest(root)
        return kth_small_node
                    
            