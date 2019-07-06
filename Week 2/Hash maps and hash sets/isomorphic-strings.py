class Solution(object):
    def isIsomorphic(self, s, t):
        """
        PROBLEM STATEMENT:
        Given two strings s and t, determine if they are isomorphic.
        Two strings are isomorphic if the characters in s can be replaced to get t.
        All occurrences of a character must be replaced with another character 
        while preserving the order of characters. 
        No two characters may map to the same character but a character may map to itself.
        :type s: str
        :type t: str
        :rtype: bool
        """     
        if len(s) != len(t):
            return False
        
        d = dict()
        c = set()
        
        for i in range(len(s)):
            if s[i] not in d and t[i] not in c:
                d[s[i]] = t[i]
                c.add(t[i])
            elif d.get(s[i]) != t[i]:
                return False
        return True
