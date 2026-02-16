"""
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = ((10000 - len(a)) * "0") + a
        b = ((10000 - len(b)) * "0") + b

        rem_bit = False
        final_array = []

        for index in range(9999, -1, -1):
            current_sum = (a[index] + b[index]).strip("0")
            if current_sum == "":
                if rem_bit:
                    final_array.append("1")
                    rem_bit = False
                else:
                    final_array.append("0")
            elif current_sum == "1":
                if rem_bit:
                    final_array.append("0")
                else:
                    final_array.append("1")
            elif current_sum == "11":
                if rem_bit:
                    final_array.append("1")
                else:
                    final_array.append("0")
                    rem_bit = True

        if rem_bit: final_array.append("1")

        final_string = ""
        while final_array:
            final_string += final_array.pop()
        final_string = final_string.lstrip("0")

        if not final_string: return "0"
        return final_string.lstrip("0")