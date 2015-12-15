class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n

        dp = [0 for i in range(n+1)]
        for j in range(3):
            dp[j] = j

        for j in range(3, n+1):
            dp[j] = dp[j-1] + dp[j-2]

        return dp[n]

