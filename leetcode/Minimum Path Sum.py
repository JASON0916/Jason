"""
Given a m x n grid filled with non-negative numbers,

find a path from top left to bottom right which minimizes the sum of all numbers along its path.
"""
__author__ = 'phoenix'


class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        if len(grid) == 0:
            return 0
        len1, len2 = len(grid), len(grid[0])
        # problems take place if you use record = [[0]*len2]*len2 shallow copy!!!
        record = [[0]*len2 for i in range(len1)]
        record[0][0] = grid[0][0]
        for i in range(1, len2):
            record[0][i] = record[0][i-1]+grid[0][i]
        for i in range(1, len1):
            record[i][0] = record[i-1][0]+grid[i][0]
        for x in range(1, len1):
            for y in range(1, len2):
                record[x][y] = min(grid[x][y]+record[x-1][y], grid[x][y]+record[x][y-1])
        return record[len1-1][len2-1]


if __name__ == '__main__':
    grid = [[7,4,8,7,9,3,7,5,0],[1,8,2,2,7,1,4,5,7],[4,6,4,7,7,4,8,2,1],[1,9,6,9,8,2,9,7,2],[5,5,7,5,8,7,9,1,4],[0,7,9,9,1,5,3,9,4]]
    print(Solution().minPathSum(grid))