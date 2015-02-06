"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.
"""

__author__ = 'phoenix'


class Solution:
    # @return an integer
    def maxArea(self, height):
        right = n = len(height) - 1
        left = 0
        res = 0
        while right != left:
            area = min(height[right], height[left]) * (right - left)
            if area > res:
                res = area
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1
        return res