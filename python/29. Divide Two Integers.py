"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""


class Solution:
    def divide(self, dividend: int, divisor: int, sign='pos') -> int:
        if abs(dividend)<abs(divisor):
            return 0
        if abs(divisor)==1:
            output = dividend if divisor>0 else -dividend
        elif dividend>0 and divisor>0:
            #print(dividend, divisor, dividend-divisor)
            output = 1 + self.divide(dividend-divisor, divisor)
        elif dividend<0 and divisor<0:
            #print(dividend, divisor, abs(dividend)-abs(divisor))
            output = 1 + self.divide(abs(dividend)-abs(divisor), abs(divisor))
        else:
            #print(dividend, divisor, -(abs(dividend)-abs(divisor)))
            output = -1 + self.divide(-(abs(dividend)-abs(divisor)), abs(divisor))
            #print('out - ',out)
        return max(-2**31, (min (output, (2**31)-1)))
# sol = Solution()
# print('out',sol.divide(-7, 2))
