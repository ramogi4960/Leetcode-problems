"""
Given a string s, find the length of the longest
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(set(s)) == 1:
            return 1

        f = 0
        for i in range(len(s) - 1):
            word = s[i]
            x = i + 1
            while x < len(s) and s[x] not in word:
                word += s[x]
                x += 1
            if len(word) > f:
                f = len(word)
        return f

