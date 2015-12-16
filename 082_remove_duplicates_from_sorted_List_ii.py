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

        delete_nums = []
        previous = head
        while previous.next:
            current = previous.next
            if current.val == previous.val:
                previous.next = current.next
                delete_nums.append(current.val)
            else:
                if previous.next:
                    previous = previous.next

        while head.val in delete_nums:
            if head.next:
                head = head.next
            else:
                return None

        previous = head
        while previous.next:
            current = previous.next
            if current.val in delete_nums:
                previous.next = current.next
            else:
                if previous.next:
                    previous = previous.next

        return head
