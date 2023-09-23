words = ["a","b","ba","bca","bda","bdca"]
words.sort(key=lambda x: len(x))


def chain(first: str, second: str) -> bool:
    final, index = '', 0
    for i in range(len(second)):
        if not index < len(first):
            final += second[i:]
            break
        if second[i] == first[index]:
            final += second[i]
            index += 1
        else:
            final += second[i]

    if len(final) - len(first) == 1 and index > len(first): return True
    return False


print(chain("abcd","dbqca"))