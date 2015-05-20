"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution:
    # @param {character[][]} board
    # @param {string} word
    # @return {boolean}
    def exist(self, board, word):
        if len(board) == 0:
            return False
        len1, len2 = len(board), len(board[0])
        def check(x, y, string):
            if len(string) == 0:
                return True
            if x < 0 or x >= len1 or y < 0 or y >= len2:
                return False
            else:
                p = board[x][y]
                visited = board[x][y] == string[0] 
                if visited:
                    board[x] = board[x][0:y] + '#' + board[x][y+1:]
                    if check(x-1, y, string[1:]) or check(x+1, y, string[1:])\
                    or check(x, y-1, string[1:]) or check(x, y+1, string[1:]):
                        return True
                    else:
                        board[x] = board[x][0:y] + p + board[x][y+1:]
                return False


        for i in range(len1):
            for j in range(len2):
                res = check(i, j, word)
                if res:
                    return res
        return False



if __name__ == '__main__':
    board = ["CAA","AAA","BCD"]
    print(Solution().exist(board, "AAB"))