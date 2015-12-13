class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_p = {'(': 1, '[': 2, '{': 3}
        right_p = {')': 1, ']': 2, '}': 3}
        if not s:
            return True

        stc = Stack()
        for ch in s:
            if ch in left_p.keys():
                stc.push(ch)
            else:
                if stc.is_empty():
                    return False
                if right_p[ch] != left_p[stc.pop()]:
                    return False
        return stc.is_empty()
