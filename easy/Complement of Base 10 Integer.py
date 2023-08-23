"""
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its
binary representation.
For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer n, return its complement.

Input: n = 5
Output: 2
Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.

Input: n = 7
Output: 0
Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.

Input: n = 10
Output: 5
Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.
"""


class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = list(bin(n)[2:])
        for i in range(len(x)):
            if x[i] == '0': x[i] = '1'
            else: x[i] = '0'

        return int(''.join(x), 2)