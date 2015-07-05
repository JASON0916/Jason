__author__ = 'phoenix'
"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""

class dict_tree_node:
    def __init__(self, cha=''):
        self.char = cha
        self.end = False
        self.next = {}

class WordDictionary:
    # initialize your data structure here.
    def __init__(self):
        self.node = dict_tree_node()

    # @param {string} word
    # @return {void}
    # Adds a word into the data structure.
    def addWord(self, word):
        pointer = self.node
        for i in range(len(word)):
            if pointer.next.get(word[i]) is None:
                pointer.next[word[i]] = dict_tree_node(word[i])
            pointer = pointer.next.get(word[i])
        pointer.end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the data structure. A word could
    # contain the dot character '.' to represent any one letter.
    def search(self, word):
        pointer = self.node

        def recursion(word, pointer):
            if len(word) == 0:
                return pointer.end
            i = 0
            while i < len(word):
                if word[i] != '.':
                    if pointer.next.get(word[i]) is not None:
                        pointer = pointer.next.get(word[i])
                        return recursion(word[i+1:], pointer)
                    else:
                        return False
                else:
                    for keys in pointer.next.keys():
                        if recursion(word[i+1:], pointer.next.get(keys)):
                            return True
                    return False
        return recursion(word, pointer)
# Your WordDictionary object will be instantiated and called as such:
# wordDictionary = WordDictionary()
# wordDictionary.addWord("word")
# wordDictionary.search("pattern")
if __name__ == '__main__':
    wordDictionary = WordDictionary()
    wordDictionary.addWord("at")
    wordDictionary.addWord("add")
    wordDictionary.addWord("and")
    wordDictionary.addWord("an")
    wordDictionary.addWord("bat")

    print(wordDictionary.search("a.d"))