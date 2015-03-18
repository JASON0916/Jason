"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
"""
__author__ = 'phoenix'


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1: return 0
        p1 = [0] * n
        p2 = [0] * n

        minV = prices[0]
        for i in range(1,n):
            minV = min(minV, prices[i])       # Find low and buy low
            p1[i] = max(p1[i - 1], prices[i] - minV)

        maxV = prices[-1]
        for i in range(n-2, -1, -1):
            maxV = max(maxV, prices[i])     # Find high and sell high
            p2[i] = max(p2[i + 1], maxV - prices[i])

        res = 0
        for i in range(n):
            res = max(res, p1[i] + p2[i])
        return res

if __name__ == '__main__':
    print(Solution().maxProfit([2,1,4]))