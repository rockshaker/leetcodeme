class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        lh = len(haystack)
        ln = len(needle)
        if ln > lh:
            return -1
        for i in range(lh-ln+1):
            j = i
            k = 0

            while j < ln + i and needle[k] == haystack[j]:
                j += 1
                k += 1

            if k == ln:
                return i

        return -1
