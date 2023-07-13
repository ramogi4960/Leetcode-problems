"""
Given two binary strings a and b, return their sum as a binary string.

Input: a = "11", b = "1"
Output: "100"

Input: a = "1010", b = "1011"
Output: "10101
"""


class Solution(object):
    def addBinary(self, a, b):
        if len(a) > len(b):
            for i in range(len(a) - len(b)):
                n = list(b)
                n.insert(0, '0')
                b = ''.join(n)
        elif len(b) > len(a):
            for i in range(len(b) - len(a)):
                n = list(a)
                n.insert(0, '0')
                a = ''.join(n)

        x, y, final = -1, 0, []
        for i in range(len(a)):
            if a[x] == '1' and b[x] == '1' and y == 0:
                final.insert(0, '0')
                y = 1
            elif a[x] == '1' and b[x] == '1' and y == 1:
                final.insert(0, '1')
                y = 1
            elif a[x] == '0' and b[x] == '0' and y == 0:
                final.insert(0, '0')
                y = 0
            elif a[x] == '0' and b[x] == '0' and y == 1:
                final.insert(0, '1')
                y = 0
            elif a[x] == '1' and b[x] == '0' and y == 0:
                final.insert(0, '1')
                y = 0
            elif a[x] == '0' and b[x] == '1' and y == 0:
                final.insert(0, '1')
                y = 0
            elif a[x] == '1' and b[x] == '0' and y == 1:
                final.insert(0, '0')
                y = 1
            elif a[x] == '0' and b[x] == '1' and y == 1:
                final.insert(0, '0')
                y = 1

            x -= 1
        if not y:
            return ''.join(final)
        else:
            final.insert(0, '1')
            return ''.join(final)