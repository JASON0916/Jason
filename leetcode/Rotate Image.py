"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
__author__ = 'phoenix'


class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix) - 1
        for i in range(n):
            for j in range(i, n-i):
                x, y = i, j
                prev = matrix[x][y]
                for k in range(4):
                    matrix[y][n-x], prev = prev, matrix[y][n-x]
                    x, y = y, n-x
        return matrix

if __name__ == '__main__':
    o = Solution()
    matrix = [[1,2,3,4],[2,3,4,1],[3,4,1,2],[4,1,2,3]]
    print(o.rotate(matrix))