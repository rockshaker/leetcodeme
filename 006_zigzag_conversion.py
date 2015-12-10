class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) < numRows:
            return s
        result_ary = [[] for i in range(numRows)]
        for i in range(len(s)):
            result_ary[self.index2rows(i, numRows)].append(s[i])

        result = ''
        for i in range(numRows):
            result += ''.join(result_ary[i])
        return result

    def index2rows(self, index, rownums):
        # 1 2 3 ... rownums-1 rownums rownums-1 ... 3 2 1  (2*rownums - 2)
        loop_length = 2 * rownums - 2
        return rownums - 1 - abs(rownums - 1 - index % loop_length)

s = Solution()
print s.convert("ABC", 2)
