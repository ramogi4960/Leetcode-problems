def rev(number: int) -> int:
    final_number = 0
    while number:
        final_number = (final_number * 10) + (number % 10)
        number //= 10

    return final_number


print(rev(123450000))