class Solution(object):
    def reverseWords(self, s):
        """
        PROBLEM STATEMENT:
        Given a string, you need to reverse the order of characters in each word within a sentence 
        while still preserving whitespace and initial word order.
        :type s: str
        :rtype: str
        """
        temp = s.split()
        for i in range(len(temp)):
            temp[i] = temp[i][::-1]
        return " ".join(temp)
