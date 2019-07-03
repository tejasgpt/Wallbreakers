class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        PROBLEM STATEMENT:
        You're given strings J representing the types of stones that are jewels, 
        and S representing the stones you have.  
        Each character in S is a type of stone you have.  
        You want to know how many of the stones you have are also jewels.
        :type J: str
        :type S: str
        :rtype: int
        """
        table = {}
        for stone in S:
            if stone in table:
                table[stone] += 1
            else:
                table[stone] = 1
        res = 0
        for jewel in J:
            if jewel in table:
                res += table[jewel]
        return res
