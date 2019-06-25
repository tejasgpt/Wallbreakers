class Solution(object):
    def detectCapitalUse(self, word):
        """
        PROBLEM STATEMENT:
        Given a word, you need to judge whether the usage of capitals in it is right or not.
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower():
            return True
        return word[0].isupper() and word[1:].islower()
        
