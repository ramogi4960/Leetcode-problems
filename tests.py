options = []
start = "12"
l = 2
while l < 10:
    options.append(int(start))
    if start[-1] == "9":
        l += 1
        start = "".join([str(item) for item in range(1, l+1)])
    else:
        temp = "".join(chr(ord(item) + 1) for item in start)
        start = temp

# print(*options, sep="\n")
print(len(options))