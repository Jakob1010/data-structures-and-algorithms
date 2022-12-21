# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        def deepestLeavesSumRec(root,level_path_sum):
            if root is None:
                return level_path_sum
            
            level_path_sum[0] += 1
            if level_path_sum[0] == level_path_sum[1]:
                level_path_sum[2] += root.val
            if level_path_sum[0] > level_path_sum[1]:
                level_path_sum[1] = level_path_sum[0]
                level_path_sum[2] = root.val
            deepestLeavesSumRec(root.left,level_path_sum)
            deepestLeavesSumRec(root.right,level_path_sum)
            level_path_sum[0] -= 1
            return level_path_sum
            
        
        return deepestLeavesSumRec(root,[0,0,0])[2]