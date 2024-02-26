fav_nums = {'Mike': 13, 'George': 28, 'Tom': 2, 'Marry': 9, 'Joseph': 5}

# number = fav_nums['Mike']
# print(f"Mike's fav num is {number}")

for person, number in fav_nums.items():
    print(f"{person}'s favorite number is {number}.")