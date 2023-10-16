def my_function(x):
    return x % 2 == 0


print(list(filter(my_function, list(range(10)))))