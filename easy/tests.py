a = [1, 2, 3, 4, 5]
for i in range(0, len(a), 2):
    try:
        x = a[i + 1]
        a[i + 1] = a[i]
        a[i] = x
    except:
        pass

print(a)