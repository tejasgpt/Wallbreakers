class Solution(object):
    def maxProfit(self, prices):
        """
        PROBLEM STATEMENT:
        Say you have an array for which the ith element is the price of a given stock on day i.
        If you were only permitted to complete at most one transaction 
        (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
        Note that you cannot sell a stock before you buy one.
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        max_profit, low = 0, prices[0]
        for i in range(1, len(prices)):
            if low < prices[i]:
                low = prices[i]
            else:
                temp = prices[i] - low
                max_profit = max(temp, max_profit)
        return max_profit
