class Solution(object):
    def calPoints(self, ops):
        """
        PROBLEM STATEMENT:
        Given a list of strings, each string can be one of the 4 following types : Integer, "+", "D", "C" 
        You need to return the sum of the points you could get in all the rounds.
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(stack[-1] * 2)
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        return sum(stack)
