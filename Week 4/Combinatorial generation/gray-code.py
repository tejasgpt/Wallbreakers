class Solution(object):
    def grayCode(self, n):
        """
        PROBLEM STATEMENT:
        The gray code is a binary numeral system where two successive values differ in only one bit.
        Given a non-negative integer n representing the total number of bits in the code, 
        print the sequence of gray code. A gray code sequence must begin with 0.
        :type n: int
        :rtype: List[int]
        """
        if n > 0:
            gray = self.grayCode(n - 1)
            rev = gray[::-1]
            return ([i for i in gray] + [j + (2** (n - 1))  for j in rev])
        else:
            return [0]
