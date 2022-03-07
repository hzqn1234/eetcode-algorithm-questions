# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Note:

# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division quotient overflows.


# too slow
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if dividend > 0 and divisor > 0:
            quotient = 0
            while dividend >= divisor:
                dividend = dividend - divisor
                quotient = quotient + 1
                print dividend
            return quotient
        if dividend > 0 and divisor < 0:
            quotient = 0
            while dividend >= (0-divisor):
                dividend = dividend + divisor
                quotient = quotient - 1
            return quotient
        if dividend < 0 and divisor > 0:
            quotient = 0
            while (0-dividend) >= divisor:
                dividend = dividend + divisor
                quotient = quotient - 1
            return quotient
        if dividend < 0 and divisor < 0:
            quotient = 0
            while dividend <= divisor:
                dividend = dividend - divisor
                quotient = quotient + 1
            return quotient
        return 0

# Long anwser, accepted
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        #
        sign = 1
        if dividend < 0:
            sign = -1
            dividend = 0 - dividend
        if divisor < 0:
            sign = 0 - sign
            divisor = 0 - divisor
        #
        final_length = len(str(dividend)) - len(str(divisor)) + 1
        if str(dividend) < str(divisor):
            final_length = final_length - 1
        #
        quotient=''
        flag = -1
        while dividend >= divisor:
            if str(dividend) >= str(divisor):
                temp_dividend = int(str(dividend)[0:len(str(divisor))])
                dividend_left = str(dividend)[len(str(divisor)):]
            else:
                temp_dividend = int(str(dividend)[0:len(str(divisor))+1])
                dividend_left = str(dividend)[len(str(divisor))+1:]
                if flag == 0 :
                    quotient = quotient + '0'
            flag = 0
            temp_quotient=0
            while temp_dividend >= divisor:
                temp_quotient = temp_quotient + 1
                temp_dividend = temp_dividend - divisor
                if temp_dividend != 0:
                    flag = 1
                else:
                    flag = 0
            dividend = int(str(temp_dividend)+dividend_left)
            quotient = quotient + str(temp_quotient)
        #
        while len(quotient) < final_length:
            quotient = quotient + '0'
        if quotient == '':
            quotient = '0'
        if sign == -1:
            result = 0-int(quotient)
        else:
            result = int(quotient)
        return result


a=Solution()
a.divide(2147483647,2)
