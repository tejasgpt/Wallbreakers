# Solution using Trie

class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word, root=None):
        if root is None:
            root = self.root
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]

    def has_prefix(self, prefix):
        root = self.root
        for c in prefix:
            if c in root:
                root = root[c]
            else:
                return False, None
        return True, root

class Solution(object):
    def longestWord(self, words):
        """
        PROBLEM STATEMENT:
        Given a list of strings words representing an English Dictionary, 
        find the longest word in words that can be built one character at a time by other words in words. 
        If there is more than one possible answer, 
        return the longest word with the smallest lexicographical order.
        If there is no answer, return the empty string.
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words)
        result = ''
        trie = Trie()
        for word in words:
            if len(word) == 1:
                trie.add(word)
                if len(word) > len(result):
                    result = word
            else:
                has_prefix, prefix_node = trie.has_prefix(word[:-1])
                if has_prefix:
                    trie.add(word[-1], prefix_node)
                    if len(word) > len(result):
                        result = word
        return result
        
# Alternate Solution

class Solution(object):
    def longestWord(self, words):
        """
        PROBLEM STATEMENT:
        Given a list of strings words representing an English Dictionary, 
        find the longest word in words that can be built one character at a time by other words in words. 
        If there is more than one possible answer, 
        return the longest word with the smallest lexicographical order.
        If there is no answer, return the empty string.
        :type words: List[str]
        :rtype: str
        """
        words = set(words)
        result = ""
        for word in words:
            if len(word) > len(result) or len(word) == len(result) and word < result:
                if all(word[:k] in words for k in range(1,len(word))):
                    result = word
        return result
