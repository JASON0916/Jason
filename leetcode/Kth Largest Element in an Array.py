"""
Find the kth largest element in an unsorted nums. Note that it is the kth largest element

in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note:
You may assume k is always valid, 1 ≤ k ≤ nums's length.
"""
__author__ = 'phoenix'


class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        if len(nums) == 0 or k > len(nums):
            return 0
        L, R = 0, len(nums)-1
        while L < R:
            low, high = L, R
            key = nums[low]
            while low < high and nums[high] < key:
                high -= 1
                nums[low] = nums[high]
            while low < high and nums[low] >= key:
                low += 1
                nums[high] = nums[low]
            nums[low] = key
            if low == k-1:
                return nums[low-1]
            elif low > k-1:
                R = low-1
            else:
                L = low + 1
        return nums[k-1]


if __name__ == '__main__':
    print(Solution().findKthLargest([3,2,1,5,6,4],2))