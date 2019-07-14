class Solution(object):
    def isSubsequence(self, s, t):
        """
        PROBLEM STATEMENT:
        Given a string s and a string t, check if s is subsequence of t.
        :type s: str
        :type t: str
        :rtype: bool
        """ 
        if len(s) > len(t):
            return False
        
        i = j = 0
        
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)
