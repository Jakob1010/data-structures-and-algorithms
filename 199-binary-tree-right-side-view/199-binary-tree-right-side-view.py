# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        output = []
        q = deque([root])
        
        while q:
            n = len(q)
            last = q[n-1]
            output.append(last.val)
            for i in range(n):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
                    
        return output
                
        
            