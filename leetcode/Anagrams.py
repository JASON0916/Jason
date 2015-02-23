"""
Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.

anagram: An anagram is a word or phrase formed by changing the order of the letters in another word or phrase.
        For example, 'triangle' is an anagram of 'integral'.
"""
__author__ = 'phoenix'


class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        dicts = {}
        res = []
        for word in strs:
            tmp_key = ''.join(sorted(word))
            temp = dicts.get(tmp_key)
            if temp is None:
                dicts[tmp_key] = [word]
            else:
                dicts[tmp_key].append(word)
        for res_key in dicts.keys():
            if len(dicts.get(res_key)) >= 2:
                res += dicts.get(res_key)
        return res

if __name__ == '__main__':
    o = Solution()
    print(o.anagrams(["tea","and","ate","eat","dan"]))