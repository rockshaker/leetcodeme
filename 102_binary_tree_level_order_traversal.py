# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        res = []
        queue = []
        queue.append(root)
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                root = queue.pop(0)
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
                level.append(root.val)
            res.append(level[:])
        return res
