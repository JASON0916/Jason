class Solution(object):
    def numSquares(self, n):
        num_map = [9999]*(n+1)
        i = 0
        while i*i <= n:
            num_map[i*i] = 1
            i += 1
        for a in range(n+1):
            b = 0
            while a+b*b <= n:
                num_map[a+b*b] = min(num_map[a]+1, num_map[a+b*b])
                b += 1
        return num_map[n]


if __name__ == '__main__':
    print Solution().numSquares(12)
