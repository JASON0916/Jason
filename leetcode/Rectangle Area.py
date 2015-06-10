class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = (C-A)*(D-B)
        area2 = (G-E)*(H-F)
        if E > C or H < B or G < A or D < F:
            return area2+ area1
        else:
            s = (min(G, C) - max(A, E))*(min(D, H) - max(B, F))
            return area1+area2-s


if __name__ == '__main__':
    print(Solution().computeArea(-2, -2, 2, 2, 1, -3, 3, -1))