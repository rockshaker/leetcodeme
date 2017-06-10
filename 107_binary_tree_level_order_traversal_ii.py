# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        queue = []
        res = []
        tres = []
        queue.append(root)
        while queue:
            n = len(queue)
            level = []
            for i in range(n):
                root = queue.pop(0)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
                level.append(root.val)
            tres.append(level[:])
        l = len(tres)
        for i in range(l-1, -1, -1):
            res.append(tres[i])
        return res
