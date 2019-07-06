class Solution(object):
    def frequencySort(self, s):
        """
        PROBLEM STATEMENT:
        Given a string, sort it in decreasing order based on the frequency of characters.
        :type s: str
        :rtype: str
        """
        import collections
        freq = collections.Counter(s)
        word = ""
        for letter in sorted(freq, key=freq.get, reverse = True):
            word += letter * freq[letter]
        return word
        
# Alternate Solution

class Solution(object):
    def frequencySort(self, s):
        """
        PROBLEM STATEMENT:
        Given a string, sort it in decreasing order based on the frequency of characters.
        :type s: str
        :rtype: str
        """
        import collections
        freq = collections.Counter(s)
        word = ""
        for letter, count in freq.most_common(len(freq)):
            word += letter * count
        return word
