"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

Example 1:
Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]


Constraints:

10 <= low <= high <= 10^9
"""


class Solution:
    def sequentialDigits(self, low: int, high: int) -> [int]:
        options = []
        start = "12"
        l = 2
        while l < 10:
            options.append(int(start))
            if start[-1] == "9":
                l += 1
                start = "".join([str(item) for item in range(1, l+1)])
            else:
                temp = "".join(chr(ord(item) + 1) for item in start)
                start = temp

        return list(filter(lambda x: low <= x <= high, options))