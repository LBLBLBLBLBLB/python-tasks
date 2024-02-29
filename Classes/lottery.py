import random

lottery_list = [10, 17, 3, 25, 68, 44, 32, 84, 11, 5, 'name', 'car', 'house', 'people', 'garden']

selected_items = random.sample(lottery_list, 4)
print(f"anyone who got {selected_items} won lottery")