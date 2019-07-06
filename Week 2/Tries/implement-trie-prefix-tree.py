class Trie(object):
    # Implement a trie with insert, search, and startsWith methods.
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        self.terminate = False
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr = self.root
        for letter in word:
            if letter not in curr:
                curr[letter] = dict()
            curr = curr[letter]
        curr[self.terminate] = True
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for letter in word:
            if letter not in curr:
                return False
            curr = curr[letter]
            
        if self.terminate in curr and curr[self.terminate] == True:
            return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
