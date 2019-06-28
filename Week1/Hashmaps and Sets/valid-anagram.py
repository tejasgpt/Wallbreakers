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
        
        table = {}
        for el in s:
            if el in table:
                table[el] += 1
            else:
                table[el] = 1
                
        for el in t:
            if el in table:
                table[el] -= 1
            else:
                return False
    
        for val in table.values():
            if val != 0:
                return False
        return True
                 
