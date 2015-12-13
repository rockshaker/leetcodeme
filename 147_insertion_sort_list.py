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
        while previous.next:
            current = previous.next
            if current.val >= previous.val:
                previous = previous.next
                continue
            previous.next = current.next
            tmp = current.next
            pos_prev = head
            while pos_prev != tmp:
                if current.val < head.val:
                    current.next = head
                    head = current
                    break
                else:
                    pos = pos_prev.next
                    if current.val < pos.val:
                        current.next = pos
                        pos_prev.next = current
                        break
                    pos_prev = pos_prev.next
        return head
