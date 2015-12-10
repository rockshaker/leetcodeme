class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        flag = 0
        if x < 0:
            x = -x
            flag = 1

        while x > 0:
            last_digit = x - x/10*10
            result = result*10 + last_digit
            x /= 10

        if flag:
            result = -result

        if result < -(1 << 31) or result > (1 << 31) - 1:
            result = 0

        return result
