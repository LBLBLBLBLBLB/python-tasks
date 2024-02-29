import random

lottery_list = [10, 17, 3, 25, 68, 44, 32, 84, 11, 5, 'name', 'car', 'house', 'people', 'garden']

my_ticket = [10, 25, 3, 'house']

attempts = 0
while True:
    attempts += 1
    selected_items = random.sample(lottery_list, 4)
    print(f"{selected_items}")
    if selected_items == my_ticket:
        print(f"i won in {attempts} attempts")
        break
