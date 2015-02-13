"""
Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""

__author__ = 'phoenix'


class Solution:
  # @param s, a string
  # @param dict, a set of string
  # @return a boolean
  def wordBreak(self, s, dict):
    sLen = len(s)
    possible = [False for i in range(sLen + 1)]
    possible[0] = True

    for i in range(sLen):
      for j in range(i + 1):
        if possible[j] and s[j:i + 1] in dict:
            possible[i + 1] = True
            break

    return possible[sLen]

"""
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    def wordBreakHelper(self, string, len_word_dict, length, flag):
        if len(string) < 1:
            return True
        for i in range(length):
            temp = len_word_dict.get(i + 1)
            if temp is None:
                continue
            else:
                if string[0:i+1] in temp:
                    if flag is False:
                        flag = self.wordBreakHelper(string[i+1:length], len_word_dict, length, flag)
                    if flag is True:
                        return True
        return False

    def wordBreak(self, s, dict):
        length = len(s)
        flag = False
        if length < 1:
            return True
        len_word_dict = {}
        # {len: [word1, word2, ... ]}
        for word in dict:
            temp = len_word_dict.get(len(word))
            if temp is None:
                len_word_dict[len(word)] = [word]
            else:
                len_word_dict[len(word)].append(word)
        return self.wordBreakHelper(s, len_word_dict, length, flag)
"""