"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
"""
__author__ = 'phoenix'


class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        i, j, length = 0, 0, 0
        while j < len(nums):
            if nums[i] == nums[j]:
                if j-i > 1:
                    nums[j-1:j] = []
                    j -= 1
            else:
                i = j
            j += 1
        return len(nums)


if __name__ == '__main__':
    nums = [1,1,2,2,2,2,2,3]
    print(Solution().removeDuplicates(nums))
    print(nums)