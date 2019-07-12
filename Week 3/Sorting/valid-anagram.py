class Solution(object):
    def isAnagram(self, s, t):
        """
        PROBLEM STATEMENT:
        Given two strings s and t , write a function to determine if t is an anagram of s.
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
