class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        n = 0
        for num in nums[1:]:
            if num != nums[n]:
                n += 1
                nums[n] = num

        return n + 1


s = Solution()
print s.removeDuplicates([1, 1, 2])
