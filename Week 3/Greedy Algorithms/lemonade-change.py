class Solution(object):
    def lemonadeChange(self, bills):
        """
        PROBLEM STATEMENT:
        At a lemonade stand, each lemonade costs $5. 
        Customers are standing in a queue to buy from you, and order one at a time 
        (in the order specified by bills).
        Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  
        You must provide the correct change to each customer, 
        so that the net transaction is that the customer pays $5.
        Note that you don't have any change in hand at first.
        Return true if and only if you can provide every customer with correct change.
        :type bills: List[int]
        :rtype: bool
        """
        change = collections.defaultdict(int)
        
        for bill in bills:
            if bill == 10:
                change[5] -= 1
            elif bill == 20:
                if change[10] > 0 :
                    change[5] -= 1
                    change[10] -= 1
                else:
                    change[5] -= 3
            if change[5] < 0:
                return False
            change[bill] += 1
            
        return True
