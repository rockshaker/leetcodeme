# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        previous = head
        current = head.next
        while not current.next:
            if current.val > previous.val:
                previous = current
                current = current.next
                continue
            tmp = current.next
            previous.next = current.next
            if current.val < head.val:
                current.next = head
                head = current
                continue
            pos_prev = head
            pos = head.next
            while pos.next != tmp:
                if pos.val > current.val:
                    pos_prev.next = current
                    current.next = pos.next
                pos_prev = pos
                pos = pos.next

        return head
