# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        count = 0
        
        def dsf(root, count):

            if not root:
                return count
            count += 1
            return max(dsf(root.left, count), dsf(root.right, count))
        
        return dsf(root, count)