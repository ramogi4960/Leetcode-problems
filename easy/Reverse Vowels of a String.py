"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"


Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        v = ''
        for item in s:
            if item in vowels:
                v += item

        v = v[::-1]
        index = 0
        final = ''
        for item in s:
            if item in vowels:
                final += v[index]
                index += 1
            else:
                final += item
        return final