class Solution(object):
    def binaryGap(self, N):
        """
        PROBLEM STATEMENT:
        Given a positive integer N, find and return the longest distance between two consecutive 1's 
        in the binary representation of N.If there aren't two consecutive 1's, return 0.
        :type N: int
        :rtype: int
        """
        prev = None
        gap = 0
        ind = 0
        while N != 0:
            if N & 1:
                if prev is not None:
                    gap = max(gap, ind - prev)
                prev = ind
            ind += 1
            N >>= 1
        return gap
