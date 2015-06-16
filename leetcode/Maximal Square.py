"""
Given a 2D binary matrix filled with 0's and 1's,

find the largest square containing all 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
__author__ = 'phoenix'


class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        if len(matrix) == 0:
            return 0
        len1, len2 = len(matrix), len(matrix[0])
        for i in range(len1):
            for j in range(len2):
                if matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1])+1
        return pow(max(max(matrix)), 2)


if __name__ == '__main__':
    matrix = [[1, 0, 1, 0, 0],
              [1, 0, 1, 1, 1],
              [1, 1, 1, 1, 1],
              [1, 0, 0, 1, 0]]
    print(Solution().maximalSquare(matrix))