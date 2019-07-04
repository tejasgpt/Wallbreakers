class Solution(object):
    def distributeCandies(self, candies):
        """
        PROBLEM STATEMENT:
        Given an integer array with even length, 
        where different numbers in this array represent different kinds of candies. 
        Each number means one candy of the corresponding kind. 
        You need to distribute these candies equally in number to brother and sister. 
        Return the maximum number of kinds of candies the sister could gain.
        :type candies: List[int]
        :rtype: int
        """
        candy_set = set()
        for candy in candies:
            candy_set.add(candy)
        
        return min(len(candy_set), len(candies)/2)
            
# ALTERNATE SOLUTION

class Solution(object):
    def distributeCandies(self, candies):
        """
        PROBLEM STATEMENT:
        Given an integer array with even length, 
        where different numbers in this array represent different kinds of candies. 
        Each number means one candy of the corresponding kind. 
        You need to distribute these candies equally in number to brother and sister. 
        Return the maximum number of kinds of candies the sister could gain.
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies)/2,len(set(candies))) 
