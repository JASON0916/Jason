__author__ = 'phoenix'
"""
Find all possible combinations of k numbers that add up to a number n,

given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Ensure that numbers within the set are sorted in ascending order.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]
"""


class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if n > 45 or k == 0:
            return []
        temp, res, nums = [], [], [1, 2, 3, 4, 5, 6, 7, 8, 9]

        def recursion(k, n, temp, res, nums):
            if n == 0 and k == 0:
                res.append(temp[:])
            elif (n > 0 and k == 0) or (n == 0 and k > 0):
                return
            else:
                for i in range(len(nums)):
                    if n-nums[i] < 0:
                        break
                    n -= nums[i]
                    temp.append(nums[i])
                    recursion(k-1, n, temp, res, nums[i+1:])
                    n += nums[i]
                    temp.pop()
        recursion(k, n, temp, res, nums)
        return res


if __name__ == '__main__':
    print Solution().combinationSum3(3, 9)