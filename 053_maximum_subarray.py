class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n^2) time complexity
        if not nums:
            maxnum = 0

        l = len(nums)
        for i in range(l):
            maxnum = nums[i]
            sumnum = nums[i]
            for j in range(i+1, l):
                sumnum += nums[j]
                maxnum = max(max, sumnum)

        return maxnum

class Solution2(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # O(n) time complexity
        dp = {}
        if not nums:
            return 0

        l = len(nums)
        dp[0] = nums[0]
        sumnums = nums[0]
        for i in range(1, l):
            # Abort the nums before, due to the sum of them are < 0
            if sumnums < 0:
                sumnums = 0
            sumnums += nums[i]
            dp[i] = max(dp[i-1], sumnums)

        return dp[l-1]

s = Solution2()
print s.maxSubArray([1, -1, 1])
