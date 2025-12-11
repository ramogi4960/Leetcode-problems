"""
No-Zero integer is a positive integer that does not contain any 0 in its decimal representation.

Given an integer n, return a list of two integers [a, b] where:

a and b are No-Zero integers.
a + b = n
The test cases are generated so that there is at least one valid solution. If there are many valid solutions, you can
return any of them.



Example 1:

Input: n = 2
Output: [1,1]
Explanation: Let a = 1 and b = 1.
Both a and b are no-zero integers, and a + b = 2 = n.
Example 2:

Input: n = 11
Output: [2,9]
Explanation: Let a = 2 and b = 9.
Both a and b are no-zero integers, and a + b = 11 = n.
Note that there are other valid answers as [8, 3] that can be accepted.


Constraints:

2 <= n <= 104
"""


class Solution:
    def getNoZeroIntegers(self, n: int) -> [int]:
        """
        Two No-Zero integers are required.
        No-Zero == positive int without zero as any of its digits.
        Start from [1, n - 1]
        Check each number as the first index increases while the second index decreases while first index < second index.
        Define a function to check each integer.
        The function should check the modulus if 0 a maximum of 4 times (1E4)
        Return the instance the two numbers are No-Zero integers
        """
        # define No-Zero checker
        def no_zero(number: int) -> bool:
            while number > 0:
                if number % 10 == 0:
                    return False
                number //= 10
            return True

        # find the two No-Zero integers
        final = [1, n - 1]

        while final[0] <= final[1]:
            if no_zero(final[0]) and no_zero(final[1]):
                return final
            final[0] += 1
            final[1] -= 1

        return final
