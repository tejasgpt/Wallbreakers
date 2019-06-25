class Solution(object):
    def hammingDistance(self, x, y):
        """
        PROBLEM STATEMENT:
        The Hamming distance between two integers is the number of positions at 
        which the corresponding bits are different.
        Given two integers x and y, calculate the Hamming distance.
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x ^ y 
        count = 0
        while xor > 0:
            if xor & 1:
                count += 1
            xor >>= 1
        return count

# Alternate Solution

class Solution(object):
    def hammingDistance(self, x, y):
        """
        PROBLEM STATEMENT:
        The Hamming distance between two integers is the number of positions at 
        which the corresponding bits are different.
        Given two integers x and y, calculate the Hamming distance.
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y)[2:].count("1")
