class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        arrays = s.split()
        if not arrays:
            return 0

        last = s.split()[-1]
        return len(last)

s = Solution()
print s.lengthOfLastWord(' ')
