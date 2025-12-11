"""
Start by defining a heapify function.
Call the heapify function from n // 2 - 1
"""

def max_heapify(arr, n, i):
    largest_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < n and arr[left_child] > arr[largest_index]:
        largest_index = left_child

    if right_child < n and arr[right_child] > arr[largest_index]:
        largest_index = right_child

    if largest_index != i:
        arr[largest_index], arr[i] = arr[i], arr[largest_index]

        max_heapify(arr, n, largest_index)