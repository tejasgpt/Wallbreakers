class Solution(object):
    def reverseVowels(self, s):
        """
        PROBLEM STATEMENT:
        Write a function that takes a string as input and reverse only the vowels of a string.
        :type s: str
        :rtype: str
        """
        s = list(s)
        vows = 'aeiouAEIOU'
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and s[left] not in vows: 
                left += 1
            while left < right and s[right] not in vows:
                right -= 1
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return "".join(s)
