class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return [1]

        l = len(digits)
        carry = 1
        for i in range(l-1, -1, -1):
            tmp = digits[i]
            digits[i] = (tmp + carry) % 10
            carry = (tmp + carry) / 10

        if carry != 0:
            digits.insert(0, carry)

        return digits

s = Solution()
print s.plusOne([0])
