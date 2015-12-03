class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a, b = b, a

        m = len(a)
        n = len(b)
        # Complete the remaining bit of b
        # Set the length of a equal with b's
        blist = []
        for i in range(n):
            blist.append(b[i])
        for j in range(m-n):
            blist.insert(0, '0')
        b = ''.join(blist)
        #
        carry = 0
        result = []

        for i in range(m):
            k = m - i - 1
            rbit = (int(a[k]) + int(b[k]) + carry) % 2
            carry = (int(a[k]) + int(b[k]) + carry) / 2
            result.insert(0, str(rbit))

        if carry == 1:
            result.insert(0, str(carry))

        result = ''.join(result)
        return result

s = Solution()
print s.addBinary("11", "1")
