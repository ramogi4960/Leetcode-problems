a = [1, 2, 3, 4, 5]
for i in range(0, len(a), 3):
    a[i:i+3] = a[i:i+3][::-1]

print(a)