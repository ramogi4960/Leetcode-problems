"""
An integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.

Given an integer n, return the largest number that is less than or equal to n with monotone increasing digits.



Example 1:

Input: n = 10
Output: 9
Example 2:

Input: n = 1234
Output: 1234
Example 3:

Input: n = 332
Output: 299


Constraints:

0 <= n <= 109
"""


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        right = ""
        n = str(n)[::-1]
        if len(n) == 1: return int(n)
        left = n[0]
        for item in n[1:]:
            if item > left[0]:
                right += "9" * len(left)
                left = item
            else:
                left = item + left

        if not right: return int(left)
        else:
            if len(set(left)) == 1: left = chr(ord(left[0]) - 1) + ("9" * len(left[1:]))
            else:
                if ord(left[-1]) > ord(left[-2]): left = left[:-1] + chr(ord(left[-1]) - 1)
                else:
                    last = -2
                    while last > -(len(left)):
                        if left[last] == left[-1]:
                            last -= 1
                        else:
                            break
                    left =  left[:last + 1] + chr(ord(left[last + 1]) - 1) + ("9" * len(left[last + 2:]))
        return int(left + right)