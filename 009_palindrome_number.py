class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = Stack()
        result = True
        for c in str(x):
            s.push(c)

        for c in str(x):
            if str(s.pop()) != c:
                result = False
                break

        return result

s = Solution()
print s.isPalindrome(0)
