"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Credits:
Special thanks to @Freezen for adding this problem and creating all test cases.
"""
__author__ = 'phoenix'


# algorithm from http://www.cnblogs.com/grandyang/p/4295761.html
class Solution:
    # @return an integer as the maximum profit
    def maxProfit2(self, prices):
        ans = 0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                ans += prices[i+1] - prices[i]
        return ans

    def maxProfit(self, k, prices):
        if len(prices) == 0:
            return 0
        if len(prices) <= k:
            return self.maxProfit2(prices)
        l = [0]*(k+1)
        g = l[:]
        for i in range(len(prices)-1):
            diff = prices[i+1] - prices[i]
            for j in range(k, 0, -1):
                l[j] = max(g[j-1] + max(diff, 0), l[j]+diff)
                g[j] = max(g[j], l[j])
        return g[k]