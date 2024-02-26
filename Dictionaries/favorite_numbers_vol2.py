fav_nums = {'Mike': [13, 14, 5, 163], 'George': [28, 12, 3, 5, 7, 9], 'Tom': [1, 12, 5, 7, 8]}

for names,nums in fav_nums.items():
    print(f'\n{names} fav nums')
    for num in nums:
        print(f'\t{num}')
