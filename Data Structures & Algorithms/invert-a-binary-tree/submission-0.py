# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        if root.left is None and root.right is not None:
            # Swap left and right
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
            return root
        if root.right is None and root.left is not None: 
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
            return root
        
        ## If both of them have, swap then call invert tree on both
        tmp = TreeNode()
        tmp = root.right
        root.right = root.left
        root.left = tmp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

