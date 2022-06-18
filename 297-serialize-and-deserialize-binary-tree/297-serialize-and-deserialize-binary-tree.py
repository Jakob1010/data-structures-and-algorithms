# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        tree = []
        def preorder(root,tree):
            if root is None:
                tree.append("N")
            else:
                tree.append(str(root.val))
                preorder(root.left,tree)
                preorder(root.right,tree)
                
        preorder(root,tree)
        return ",".join(tree)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return
        
        tree = data.split(',')
        self.i = 0
        def preorder(tree):
            if tree[self.i] == 'N':
                self.i += 1
                return None
            
            root = TreeNode(tree[self.i])
            self.i += 1
            root.left = preorder(tree)
            root.right = preorder(tree)            
            
            return root
            
        return preorder(tree)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))