"""
You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""
__author__ = 'phoenix'


class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        if len(L) == 0:
            return []
        dict_temp = {key: False for key in L}
        dict_L = dict_temp.copy()
        start = end = 0
        len_w, len_L = len(L[0]), len(L)
        res = []
        while end < len(S) - len_w + 1:
            if S[end: end+len_w] in L:
                dict_temp[S[end: end+len_w]] = True
                end += len_w
            else:
                end += 1
                if dict_temp != dict_L:
                    dict_temp = dict_L.copy()
                start = end
            if False not in dict_temp.values():
                dict_temp = dict_L.copy()
                res.append(start)
                start = end
        return res



if __name__ == '__main__':
    S = "a"
    L = ["a"]
    print(Solution().findSubstring(S, L))