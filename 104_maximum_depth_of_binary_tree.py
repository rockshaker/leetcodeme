# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        maxl = 0
        maxr = 0
        if root.left:
            maxl = self.maxDepth(root.left)
        if root.right:
            maxr = self.maxDepth(root.right)

        maxdepth = max(maxl, maxr)
        return maxdepth + 1
