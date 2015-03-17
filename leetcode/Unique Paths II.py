"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
__author__ = 'phoenix'


class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        if 1 in obstacleGrid[0]:
            index1 = obstacleGrid[0].index(1)
        else:
            index1 = n
        obstacleGrid[0][:index1] = [1]*index1
        obstacleGrid[0][index1:] = [0]*(n-index1)
        index2 = m
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                obstacleGrid[i][0] = 1
            else:
                index2 = i
                break
        for i in range(index2, m):
            obstacleGrid[i][0] = 0
        for x in range(1, m):
            for y in range(1, n):
                if obstacleGrid[x][y] == 1:
                    obstacleGrid[x][y] = 0
                else:
                    obstacleGrid[x][y] = obstacleGrid[x-1][y] + obstacleGrid[x][y-1]
        return obstacleGrid[m-1][n-1]


if __name__ == '__main__':
    o = Solution()
    matrix = [[0,0,0],[0,1,0],[0,0,0]]
    print(o.uniquePathsWithObstacles(matrix))