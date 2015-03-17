"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
"""
__author__ = 'phoenix'


class Solution1:
    # @return an integer
    def uniquePaths(self, m, n):
        res = []
        for _ in range(m):
            res.append([1]*n)
        for x in range(1, m):
            for y in range(1, n):
                res[x][y] = res[x-1][y] + res[x][y-1]
        return res[m-1][n-1]


class Solution:
    # @return an integer
    def get_factorial(self, x):
        if x == 0:
            return 1
        else:
            return x * self.get_factorial(x-1)

    def uniquePaths(self, m, n):
        return int(self.get_factorial(m+n-2)/(self.get_factorial(m-1)*self.get_factorial(n-1)))


if __name__ == '__main__':
    o = Solution()
    print(o.uniquePaths(2, 2), '\n')
    print(o.uniquePaths(3, 2), '\n')