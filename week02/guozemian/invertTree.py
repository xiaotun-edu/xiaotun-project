# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return None
        res = []
        a = TreeNode()
        def dsf(root,a):
            if not root:
                return

            a.val = root.val
            
            res.append(root.val)
            if root.left:
                a.right = TreeNode()
                dsf(root.left, a.right)

            if root.right:
                a.left = TreeNode()
                dsf(root.right, a.left)

        dsf(root, a)
        
        return a