nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
new_nums = []
for item in nums:
    if new_nums.count(item) < 2:
        new_nums.append(item)
    else:
        pass

for i in range(len(nums)):
    try:
        nums[i] = new_nums[i]
    except:
        pass
print(new_nums)
print(nums)