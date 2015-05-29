"""
Implement a trie with insert, search, and startsWith methods.
"""
import datetime


class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.next = {}
        self.end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        loc = self.root
        while len(word) > 0 and loc.next.get(word[0]) is not None:
            loc = loc.next[word[0]]
            word = word[1:]
        while len(word) > 0:
            tis = loc.next[word[0]] = TrieNode()
            loc = tis
            word = word[1:]
        loc.end = True

    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        loc = self.root
        while len(word) > 0 and loc.next.get(word[0]) is not None:
            loc = loc.next[word[0]]
            word = word[1:]
        if len(word) == 0 and loc.end is True:
            return True
        else:
            return False

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def startsWith(self, prefix):
        loc = self.root
        while len(prefix) > 0 and loc.next.get(prefix[0]) is not None:
            loc = loc.next[prefix[0]]
            prefix = prefix[1:]
        if len(prefix) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    start = datetime.datetime.now()
    t = Trie()
    t.insert("abort")
    t.insert("apple")
    print(t.search("abo"))
    print(t.startsWith("abo"))
    end = datetime.datetime.now()
    print(end - start)