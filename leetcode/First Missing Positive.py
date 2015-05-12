__author__ = 'phoenix'
"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
"""


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        if len(nums) == 0:
            return 1
        for i in range(len(nums)):
            while nums[i] != i+1:
                if nums[i] > len(nums) or nums[i] <= 0 or nums[i] == nums[nums[i]-1]:
                    break
                else:
                    temp = nums[i]
                    nums[i] = nums[nums[i]-1]
                    nums[temp-1] = temp
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums)+1


if __name__ == '__main__':
    print(Solution().firstMissingPositive([3,4,0,2]))
