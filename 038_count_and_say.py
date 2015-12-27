class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
    def countAndSay(self, n):
        if n == 0:
            return ''

        if n == 1:
            return '1'

        prev = self.countAndSay(n-1)
        prev_l = len(prev)
        i = 1
        res = []
        last_repeat = False
        while i < prev_l:
            count = 1
            while prev[i] == prev[i-1]:
                count += 1
                i += 1
                if i == prev_l:
                    last_repeat = True
                    break

            res.append(str(count))
            res.append(prev[i-1])
            i += 1

        if not last_repeat:
            res.append('1')
            res.append(prev[-1])
        return ''.join(res)

s = Solution()
print s.countAndSay(5)
