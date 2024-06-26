"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letters = {}
        index = 0
        s = s.split()
        if len(s) != len(pattern): return False
        while index < len(pattern):
            try: x = letters[pattern[index]]
            except:
                if s[index] in letters.values(): return False
                else: letters[pattern[index]] = s[index]
            else:
                if x != s[index]: return False
            finally: index += 1
        return True
