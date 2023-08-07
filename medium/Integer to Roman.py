"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.
- Given an integer, convert it to a roman numeral.

Input: num = 3
Output: "III"
Explanation: 3 is represented as 3 ones.

Input: num = 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.

Input: num = 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        x = str(num)
        roman = {
            '0': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V',
            '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', '10': 'X',
            '11': 'XI', '12': 'XII', '13': 'XIII', '14': 'XIV', '15': 'XV', '16': 'XVI',
            '17': 'XVII', '18': 'XVIII', '19': 'XIX', '20': 'XX', '30': 'XXX',
            '40': 'XL', '50': 'L', '60': 'LX', '70': 'LXX', '80': 'LXXX', '90': 'XC',
            '100': 'C', '200': 'CC', '300': 'CCC', '400': 'CD', '500': 'D',
            '600': 'DC', '700': 'DCC', '800': 'DCCC', '900': 'CM',
        }

        def tens(n: str) -> str:
            if n[0] == '0':
                return roman[n[-1]]
            elif int(n) < 20:
                return roman[n]
            elif n[-1] == '0':
                return roman[n]
            else:
                return roman[n[0] + '0'] + roman[n[-1]]

        def hundreds(n: str) -> str:
            if n[1:] == '00':
                return roman[n]
            elif n[0] == '0':
                return tens(n[1:])
            else:
                return roman[n[0] + '00'] + tens(n[1:])

        def thousands(n: str) -> str:
            if n[1:] == '000': return int(n[0]) * 'M'
            return (int(n[0]) * 'M') + hundreds(n[1:])

        if len(x) == 1:
            return roman[x]
        elif len(x) == 2:
            return tens(x)
        elif len(x) == 3:
            return hundreds(x)
        else:
            return thousands(x)