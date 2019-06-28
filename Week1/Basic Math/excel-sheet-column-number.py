class Solution(object):
    def titleToNumber(self, s):
        """
        PROBLEM STATEMENT:
        Given a column title as appear in an Excel sheet, return its corresponding column number.
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        return 26 * self.titleToNumber(s[:-1]) + ord(s[-1]) - 64
            
        
