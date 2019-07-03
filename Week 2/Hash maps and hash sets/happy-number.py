class Solution(object):
    def isHappy(self, n):
        """
        PROBLEM STATEMENT:
        Write an algorithm to determine if a number is "happy".
        A happy number is a number defined by the following process: 
        Starting with any positive integer, 
        replace the number by the sum of the squares of its digits, 
        and repeat the process until the number equals 1 (where it will stay), 
        or it loops endlessly in a cycle which does not include 1. 
        Those numbers for which this process ends in 1 are happy number
        :type n: int
        :rtype: bool
        """
        def nextNumber(n):
            new = 0
            for char in str(n):
                new += int(char)**2
            return new
        
        lookup = {}
        while n != 1 and n not in lookup:
            lookup[n] = True
            n = nextNumber(n)
        return n == 1

    
