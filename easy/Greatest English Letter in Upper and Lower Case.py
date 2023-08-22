"""
Given a string of English letters s, return the greatest English letter which occurs as both a lowercase and uppercase
letter in s. The returned letter should be in uppercase. If no such letter exists, return an empty string.
An English letter b is greater than another letter a if b appears after a in the English alphabet.

Input: s = "lEeTcOdE"
Output: "E"
Explanation:
The letter 'E' is the only letter to appear in both lower and upper case.

Input: s = "arRAzFif"
Output: "R"
Explanation:
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.

Input: s = "AbCdEfGhIjK"
Output: ""
Explanation:
There is no letter that appears in both lower and upper case.
"""


class Solution:
    def greatestLetter(self, s: str) -> str:
        x = []
        for item in s:
            if item.upper() in s and item.lower() in s and (item.upper(), item.lower()) not in x:
                x.append((item.upper(), item.lower()))

        if not x: return ''

        x.sort(key=lambda y: y[0])
        return x[-1][0]
