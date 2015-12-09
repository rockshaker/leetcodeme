# Definition for singly-linked list.
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        current = head
        l = 1
        while current.next:
            l += 1
            current = current.next

        current.next = head

        step = l - k % l
        while step > 0:
            step -= 1
            current = current.next

        nhead = current.next
        current.next = None
        return nhead
