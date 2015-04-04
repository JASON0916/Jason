"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house,
determine the maximum amount of money you can rob tonight without alerting the police.

Credits:
Special thanks to @ifanchu for adding this problem and creating all test cases.
Also thanks to @ts for adding additional test cases.
"""
__author__ = 'phoenix'


class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
        if len(num) == 1:
            return num[0]
        res = [0] * (len(num)+1)
        res[1] = num[0]
        for i in range(2, len(num)+1):
            res[i] = max(res[i-2] + num[i-1], res[i-1])
        return res[len(num)]


if __name__ == '__main__':
    print(Solution().rob([1,2]))