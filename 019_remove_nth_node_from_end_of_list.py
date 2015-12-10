# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast = head

        if n == 0:
            return head
        if head.next is None and n == 1:
            return None

        while fast.next is not None:
            if n > 0:
                fast = fast.next
                n -= 1
            else:
                slow = slow.next
                fast = fast.next

        # This represent n equal the size of this list
        if n:
            head = slow.next

        delete_node = slow.next
        slow.next = delete_node.next

        return head
