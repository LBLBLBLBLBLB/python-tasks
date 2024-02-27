sandwich_orders = ["Club", "Pastrami",  "Turkey", "Pastrami", "Vegetarian", "Chicken Salad", "Tuna", "Pastrami"]

finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f'I made you {sandwich}')
    finished_sandwiches.append(sandwich)

for finished in finished_sandwiches:
    print(f'finished sandwich is {finished}')