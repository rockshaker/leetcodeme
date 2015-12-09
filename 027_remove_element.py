class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = 0
        for num in nums:
            if num != val:
                nums[n] = num
                n += 1

        return n

s = Solution()
print s.removeElement([4, 5], 4)
