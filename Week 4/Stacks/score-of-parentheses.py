class Solution(object):
    def scoreOfParentheses(self, S):
        """
        PROBLEM STATEMENT:
        Given a balanced parentheses string S, compute the score of the string based on the following rule
        () has score 1
        AB has score A + B, where A and B are balanced parentheses strings.
        (A) has score 2 * A, where A is a balanced parentheses string.
        :type S: str
        :rtype: int
        """
        stack = [0] 

        for s in S:
            if s == '(':
                stack.append(0)
            else:
                para = stack.pop()
                stack[-1] += 2 * para or 1

        return stack.pop()
