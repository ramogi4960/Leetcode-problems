"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Input: n = 1
Output: true
Explanation: 20 = 1

Input: n = 16
Output: true
Explanation: 24 = 16

Input: n = 3
Output: false
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        x = 1
        while -2**31 <= 2**x <= 2**31-1:
            if 2**x == n:
                return True
            x += 1
        return False