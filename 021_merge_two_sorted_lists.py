# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = None
        res_end = None
        while l1 and l2:
            if l1.val < l2.val:
                if not res:
                    res = l1
                    res_end = res
                else:
                    res_end.next = l1
                    res_end = res_end.next
                l1 = l1.next
            else:
                if not res:
                    res = l2
                    res_end = res
                else:
                    res_end.next = l2
                    res_end = res_end.next
                l2 = l2.next

        if l1:
            if not res:
                res = l1
            else:
                res_end.next = l1
        if l2:
            if not res:
                res = l2
            else:
                res_end.next = l2
        return res
