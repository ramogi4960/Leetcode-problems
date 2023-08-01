"""
Given a string s, return the longest palindromic substring in s.

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Input: s = "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(set(s)) == len(s):
            return s[0]
        f = ''
        for i in range(len(s) - 1):
            x = s[i]
            r = i+1
            while r < len(s):
                x += s[r]
                if x[::-1] == x and len(x) > len(f):
                    f = x
                r += 1
        if not f:
            return s[0]
        else:
            return f
