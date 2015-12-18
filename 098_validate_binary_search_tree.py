# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        INT_MIN = -2**64
        INT_MAX = 2**64 - 1
        return self.isValidBSTImp(root, INT_MIN, INT_MAX)

    def isValidBSTImp(self, root, minn, maxn):
        if not root:
            return True
        return minn < root.val < maxn \
               and self.isValidBSTImp(root.left, minn, root.val) \
               and self.isValidBSTImp(root.right, root.val, maxn)
