class Solution(object):
    def wordPattern(self, pattern, words):
        """
        PROBLEM STATEMENT:
        Given a pattern and a string str, find if str follows the same pattern.
        Here follow means a full match, such that there is a bijection between a letter in pattern 
        and a non-empty word in str.
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not words:
            return False
        
        word = words.split()
        if len(pattern) != len(word):
            return False
        
        d = dict()
        c = set()
        for i in range(len(pattern)):
            if pattern[i] not in d and word[i] not in c:
                d[pattern[i]] = word[i]
                c.add(word[i])
            elif d.get(pattern[i]) != word[i]:
                return False
        return True
