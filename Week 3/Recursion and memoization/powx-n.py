class Solution(object):
    def myPow(self, x, n):
        """
        PROBLEM STATEMENT:
        Implement pow(x, n), which calculates x raised to the power n.
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2)
