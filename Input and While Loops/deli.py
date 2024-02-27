sandwich_orders = ["Club", "Turkey", "Ham and Cheese", "Vegetarian", "Chicken Salad", "Tuna", "Grilled Cheese"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made you {sandwich}')
    finished_sandwiches.append(sandwich)

for finished in finished_sandwiches:
    print(f'finished sandwich is {finished}')
    