"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Input: s = "A", numRows = 1
Output: "A"
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        if numRows == 2:
            x, y, z = [], [], True
            for i in range(len(s)):
                if z:
                    x.append(s[i])
                    z = False
                else:
                    y.append(s[i])
                    z = True
            return ''.join(x+y)
        # first we create a matrix of rows=numRows
        # we then iterate through s while appending rows in the matrix
        matrix, a, count = [[] for _ in range(numRows)], True, 0
        for item in s:
            if a:
                matrix[count].append(item)
                count += 1
                if count == numRows:
                    a = False
                    count -= 2
            else:
                matrix[count].append(item)
                count -= 1
                if count == -1:
                    a = True
                    count += 2
        final = ''
        for item in matrix:
            final += "".join(item)
        return final