class Solution(object):
    def generateParenthesis(self, n):
        """
        PROBLEM STATEMENT:
        Given n pairs of parentheses, 
        write a function to generate all combinations of well-formed parentheses.
        For example, given n = 3, a solution set is:
        :type n: int
        :rtype: List[str]
        """
        paragraph = [['']]
        for num in range(1, n + 1):
            generate = []
            for i in range(num):
                for j in paragraph[i]:
                    for k in paragraph[num - i - 1]:
                        generate.append('(' + j + ')' + k)
            paragraph.append(generate)
        return paragraph[n]
