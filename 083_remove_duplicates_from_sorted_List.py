# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        previous = head
        while previous.next:
            current = previous.next
            if current.val == previous.val:
                previous.next = current.next
            else:
                if previous.next:
                    previous = previous.next

        return head
