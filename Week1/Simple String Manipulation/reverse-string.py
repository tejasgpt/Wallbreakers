class Solution(object):
    def reverseString(self, s):
        """
        PROBLEM STATEMENT:
        Write a function that reverses a string. 
        The input string is given as an array of characters char[].
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            right-=1
            left+=1
        return s
       
# Alternate Solution

class Solution(object):
    def reverseString(self, s):
        """
        PROBLEM STATEMENT:
        Write a function that reverses a string. 
        The input string is given as an array of characters char[].
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)/2):
             s[i], s[len(s)-i-1] = s[len(s)-i-1], s[i]
