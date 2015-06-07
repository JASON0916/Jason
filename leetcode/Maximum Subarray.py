"""
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""
__author__ = 'phoenix'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        (sub_big, sub_small, res) = ([nums[0]]*3)
        for i in range(1, len(nums)):
            sub_big = max(nums[i], sub_big+nums[i])
            res = max(sub_big, res)
        return res


if __name__ == '__main__':
    array = [-2, 1,-3,4,-1, 2,1,-5,4]
    print(Solution().maxSubArray(array))