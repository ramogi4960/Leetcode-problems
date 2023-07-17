"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the
signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Input: x = 123
Output: 321

Input: x = -123
Output: -321

Input: x = 120
Output: 21

-231 <= x <= 231 - 1
"""


class Solution(object):
    def reverse(self, x):
        a = list(str(x))
        if a[0] == '-':
            new_a = a[1:]
            new_a = new_a[::-1]
            while new_a[0] == '0':
                del new_a[0]
            new_a = int('-' + ''.join(new_a))
            if -2**31 <= new_a <= 2**31 - 1:
                return new_a
            else:
                return 0
        else:
            if 0 <= x < 10:
                return x
            else:
                new_a = a[::-1]
                while new_a[0] == '0':
                    del new_a[0]
                new_a = int(''.join(new_a))
                if -2**31 <= new_a <= 2**31 - 1:
                    return new_a
                else:
                    return 0