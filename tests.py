def sum_of_ints(nums: [int], goal: int) -> int:
    if goal == 0:
        start = 0
        count = 0
        while start < len(nums):
            if nums[start] == 0:
                count += 1
                try: end = start + 1
                except: start += 1
                else:
                    while end < len(nums):
                        if nums[end] == 0:
                            count += end - start + 1
                            end += 1
                        else:
                            start = end
            else:
                start += 1
        return count


print(sum_of_ints([0, 1, 0, 1, 0], 0))