# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        each = []
        self.pathSumImp(root, sum, each, res)
        return res

    def pathSumImp(self, root, sum, each, res):
        if not root:
            return
        if not root.left and not root.right:
            if root.val == sum:
                each.append(root.val)
                res.append(each[:])
                each.pop()
        else:
            each.append(root.val)
            self.pathSumImp(root.left, sum-root.val, each, res)
            self.pathSumImp(root.right, sum-root.val, each, res)
            each.pop()
