"""
Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
"""
__author__ = 'phoenix'


class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if len(board) == 0:
            return
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != "O":
                return
            board[x] = board[x][:y] + 'S' + board[x][y+1:]
            dfs(x-1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y)

        for i in range(n):
            dfs(0, i)
            dfs(m-1, i)

        for j in range(m):
            dfs(j, 0)
            dfs(j, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i] = board[i][:j] + 'X' + board[i][j+1:]
                if board[i][j] == 'S':
                    board[i] = board[i][:j] + 'O' + board[i][j+1:]


if __name__ == '__main__':
    o = Solution()
    matrix = ["O"]
    o.solve(matrix)
    print(matrix)