# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        def dsf(root):
            if not root:
                return 
            dsf(root.left)
            dsf(root.right)
            res.append(root.val)

        dsf(root)

        return res