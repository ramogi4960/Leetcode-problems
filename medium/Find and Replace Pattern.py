"""
Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return
the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the
pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and
no two letters map to the same letter.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]


Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.
"""


class Solution:
    def findAndReplacePattern(self, words: [str], pattern: str) -> [str]:
        # create a function for checking two strings
        def checker(string1, string2) -> bool:
            my_dict = {}
            for i in range(len(string1)):
                try:
                    if my_dict[string1[i]] != string2[i]:
                        return False
                except:
                    if string2[i] in my_dict.values():
                        return False
                    my_dict[string1[i]] = string2[i]


            return True

        final = []
        for item in words:
            if checker(pattern, item):
                final.append(item)

        return final