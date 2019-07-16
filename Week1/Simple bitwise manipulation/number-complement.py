class Solution(object):
    def findComplement(self, num):
        """
        PROBLEM STATEMENT:
        Given a positive integer, output its complement number. 
        The complement strategy is to flip the bits of its binary representation.
        :type num: int
        :rtype: int
        """
        complement = ""
        for bn in bin(num)[2:]:
            complement += str(1 - int(bn)) # Invert 0s and 1s
        return int(complement,2) # Return integer representation of complement
