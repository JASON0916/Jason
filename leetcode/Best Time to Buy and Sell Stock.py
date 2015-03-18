"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock),

design an algorithm to find the maximum profit.
"""
__author__ = 'phoenix'


class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        low = prices[0]
        ans = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            elif prices[i] - low > ans:
                ans = prices[i] - low
        return ans


if __name__ == '__main__':
    o = Solution()
    prices1 = [3,2,6,5,0,3]
    print(o.maxProfit(prices1),'\n')
    prices2 = [4,0,3]
    print(o.maxProfit(prices2))