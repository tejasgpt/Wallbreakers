class Solution(object):
    def fizzBuzz(self, n):
        """
        PROBLEM STATEMENT:
        Write a program that outputs the string representation of numbers from 1 to n.
        But for multiples of three it should output “Fizz” instead of the number 
        and for the multiples of five output “Buzz”. 
        For numbers which are multiples of both three and five output “FizzBuzz”.
        :type n: int
        :rtype: List[str]
        """
        output = []
        for num in range(1,n+1):
            if num % 3 == 0:
                if num % 5 == 0:
                    output.append("FizzBuzz")
                else:
                    output.append("Fizz")
            else:
                if num % 5 == 0:
                    output.append("Buzz")
                else:
                    output.append(str(num))
        return output
                    
