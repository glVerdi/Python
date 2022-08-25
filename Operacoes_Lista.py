nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums, '\n')

nums = [1, 2, 3, 4, 5]
nums[3] = nums[1]
print(nums[3], '\n')

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3, '\n')

nums = [33, 42, 56]
nums[1] = 22
print(nums, '\n')

words = ['spam' , 'egg', 'spam', 'sausege']
print('spam' in words)
print('egg' in words)
print('tomato' in words, '\n')

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4], '\n')

nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums, '\n')

letters = ['a', 'b', 'z']
if 'z' in letters:
    print('yes \n')

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]], '\n')