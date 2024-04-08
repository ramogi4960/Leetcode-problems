"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.



Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""


Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Iteratet through the string.
        Iteration continues so long as str1[index] == str2[index] and index < len(str1) and len(str2).
        Through each iteration, check if len(str1) % len(final) == 0 and len(str2) % len(final) == 0
        if so, record final.
        """
        final, index = "", 0
        output = ""
        word_length = 0
        first, second = len(str1), len(str2)
        while index < first:
            try:
                if str1[index] == str2[index]:
                    final += str1[index]
                    word_length += 1
                    if first % word_length == 0 and final * (
                            first // word_length) == str1 and second % word_length == 0 and final * (
                            second // word_length):
                        output = final

                else:
                    return ""
            except:
                break
            index += 1

        return output