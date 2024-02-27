dream_vacations = {}

print("Welcome to the Dream Vacation Poll!")
print("Enter 'quit' anytime to end the poll.\n")

while True:
    response = input("If you could visit one place in the world, where would you go? ")

    if response.lower() == 'quit':
        break

    if response in dream_vacations:
        dream_vacations[response] += 1
    else:
        dream_vacations[response] = 1

print("\n--- Poll Results ---")
for destination, votes in dream_vacations.items():
    print(f"{destination}: {votes} vote(s)")