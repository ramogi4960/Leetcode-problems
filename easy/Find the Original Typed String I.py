"""
Alice is attempting to type a specific string on her computer. However, she tends to be clumsy and may press a key for
too long, resulting in a character being typed multiple times.

Although Alice tried to focus on her typing, she is aware that she may still have done this at most once.

You are given a string word, which represents the final output displayed on Alice's screen.

Return the total number of possible original strings that Alice might have intended to type.



Example 1:

Input: word = "abbcccc"

Output: 5

Explanation:

The possible strings are: "abbcccc", "abbccc", "abbcc", "abbc", and "abcccc".

Example 2:

Input: word = "abcd"

Output: 1

Explanation:

The only possible string is "abcd".

Example 3:

Input: word = "aaaa"

Output: 4



Constraints:

1 <= word.length <= 100
word consists only of lowercase English letters.
"""

class Solution:
    def possibleStringCount(self, word: str) -> int:
        """
        Alice may have made the mistake either once or never.
        The only time she makes a mistake is when there is a repeated character/letter.
        If there are no repeated characters, then there is no mistake.
        """
        # possible_string_count will always be > 0 considering the string without a mistake
        # create a variable to represent the final return value.
        possible_str_count:int = 1
        # a repeated character is equivalent to word[i] == word[i + 1] for 0 <= i < len(word) - 1
        # iterate through words
        for i in range(0, len(word) - 1):
            possible_str_count += 1 if word[i] == word[i + 1] else 0

        return possible_str_count

