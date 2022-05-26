# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        output = []
        pq = [-float('inf')]
        
        def DFS(root):
            if root is None:
                return
            
            if root.val >= pq[-1]:
                output.append(root.val)
            pq.append(max(root.val,pq[-1]))
            DFS(root.left)
            DFS(root.right)
            pq.pop(-1)
          
        DFS(root)
        return len(output)