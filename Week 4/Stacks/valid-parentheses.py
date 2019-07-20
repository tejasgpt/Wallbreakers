class Solution(object):
    def isValid(self, s):
        """
        PROBLEM STATEMENT:
        Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
        determine if the input string is valid.
        An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        
        stack = []
        opened = {"(":")","[":"]","{":"}"}
        for st in s:
            if st in opened:
                stack.append(st)
            else:
                if len(stack) < 1:
                    return False 
                if opened[stack.pop()] != st:
                    return False
        return len(stack) == 0
                
