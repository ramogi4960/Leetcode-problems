"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
represent. Return the answer in any order.

On a phone, the numbers represent letters that can be used to text. For example, 2 carries a, b and c, 3 carries d, e
and f...

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Input: digits = ""
Output: []

Input: digits = "2"
Output: ["a","b","c"]
"""


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        my_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        a = []
        for item in digits:
            a.append(my_dict[item])
        x = []
        if len(a) == 1:
            return a[0]
        elif len(a) == 2:
            for i in a[0]:
                for j in a[1]:
                    x.append(i + j)
            return x
        elif len(a) == 3:
            for i in a[0]:
                for j in a[1]:
                    for k in a[2]:
                        x.append(i + j + k)
            return x
        else:
            for i in a[0]:
                for j in a[1]:
                    for k in a[2]:
                        for l in a[3]:
                            x.append(i + j + k + l)
            return x
