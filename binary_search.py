"""
This is a reusable function for searching for an integer from an sorted array
It returns a True if the integer exists within the array, else False.
"""


def binary_search(array: [int], n: int) -> str:
    count = 0
    mid = len(array)//2
    while len(array) > 1:
        if array[mid] == n:
            count += 1
            return f"{True}\nNumber of steps taken: {count}"
        elif array[mid] > n:
            array = array[:mid]
            mid = len(array)//2
            count += 1
        else:
            array = array[mid:]
            mid = len(array)//2
            count += 1

    return f"{array[0] == n}\nNumber of steps taken: {count}"

