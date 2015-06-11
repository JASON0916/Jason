__author__ = 'phoenix'
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
"""


class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0:
            return False
        global x
        length1, length2, x = len(matrix), len(matrix[0]), 0
        if matrix[length1-1][0] < target:
            x = length1-1
        else:
            for i in range(length1-1):
                if matrix[i][0] < target < matrix[i+1][0]:
                    x = i
                if matrix[i][0] == target or matrix[i+1][0] == target:
                    return True
        start, end = 0, length2-1
        while end >= start:
            mid = int((start+end)/2)
            if matrix[x][mid] > target:
                end = mid-1
            elif matrix[x][mid] < target:
                start = mid+1
            else:
                return True
        return False

if __name__ == '__main__':
    matrix = [[1],[3]]
    print(Solution().searchMatrix(matrix,3))