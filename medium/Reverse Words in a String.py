"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only
 have a single space separating the words. Do not include any extra spaces.

Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
"""

from re import split


class Solution:
    def reverseWords(self, s: str) -> str:
        # the string can have leading and trailing spaces in which we can use strip()
        # to get the words, we can split() using a regex since there can be more than one space
        # we then reverse that list we've gotten from split()
        # finally, we join the reversed list with a single space
        return ' '.join(split(r'\s+', s.strip())[::-1])