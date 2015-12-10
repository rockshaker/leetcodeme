# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        carry = 0
        res = None
        res_end = None
        while l1 and l2:
            tsum = l1.val + l2.val + carry
            digit = tsum % 10
            carry = tsum / 10
            if not res:
                res = ListNode(digit)
                res_end = res
            else:
                res_end.next = ListNode(digit)
                res_end = res_end.next
            l1 = l1.next
            l2 = l2.next

        rem = None
        if l1:
            rem = l1
        if l2:
            rem = l2

        if rem:
            while rem:
                tsum = rem.val + carry
                digit = tsum % 10
                carry = tsum / 10
                res_end.next = ListNode(digit)
                res_end = res_end.next
                rem.next = rem
        if carry == 1:
            res_end.next = ListNode(1)

        return res


class Solution2(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = None
        res_end = None

        while l1 or l2 or carry == 1:
            tmp = 0
            if l1:
                tmp += l1.val
                l1 = l1.next
            if l2:
                tmp += l2.val
                l2 = l2.next
            tmp += carry

            digit = tmp % 10
            carry = tmp / 10
            if not res:
                res = ListNode(digit)
                res_end = res
            else:
                res_end.next = ListNode(digit)
                res_end = res_end.next

        return res
