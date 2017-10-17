class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l < 2:
            return 0

        minp = prices[0]
        profit = prices[1] - prices[0]

        for i in range(2, l):
            minp = min(minp, prices[i-1])
            profit = max(profit, prices[i] - minp)

        if profit < 0:
            return 0

        return profit


if __name__ == "__main__":
    s = Solution()
    t1 = [1, 2, 3, 3, 0]
    res = s.maxProfit(t1)
    print res

    t2 = [7, 4, 3, 2]
    res = s.maxProfit(t2)
    print res
