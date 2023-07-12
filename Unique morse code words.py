# in this task, we are supposed to return a morse code representation of a given string
# each letter has its own unique moser code equivalent
# a full word in morse code is the concatenation of the morse code of each letter

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse_code_letters = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-",
                              ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-",
                              ".--", "-..-", "-.--", "--.."]
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        final = set()
        for item in words:
            a = ''
            for i in item:
                a += morse_code_letters[alphabet.index(i)]
            final.add(a)
        return len(final)

"""
input: words = ["gin","zen","gig","msg"]
output: 2
"""
x = Solution()
print(x.uniqueMorseRepresentations(input().split()))
