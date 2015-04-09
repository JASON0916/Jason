"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
"""
__author__ = 'phoenix'


class Solution:
    # @param grid, a list of list of characters
    # @return an integer
    def check(self, grid, x, y):
        if y < 0 or y >= len(grid[0]):
            return
        if x < 0 or x >= len(grid):
            return
        if grid[x][y] != "1":
            return
        grid[x] = grid[x][0:y] + 'X' + grid[x][y+1:]
        self.check(grid, x-1, y)
        self.check(grid, x+1, y)
        self.check(grid, x, y-1)
        self.check(grid, x, y+1)

    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        x, y = len(grid[0]), len(grid)
        res = 0
        for i in range(y):
            for j in range(x):
                if grid[i][j] == '1':
                    self.check(grid, i, j)
                    res += 1
        return res


if __name__ == '__main__':
    grid = ["11"]
    print(Solution().numIslands(grid))