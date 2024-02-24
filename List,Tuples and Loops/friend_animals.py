animals = ['wolf', 'dog', 'fox']

for animal in animals:
    print(animal)

friend_animals = animals[:]
print(friend_animals)
animals.append('lion')
friend_animals.append('tiger')


print(f'my favorite animals are {animals}')
print(f'friends favorite animals are {friend_animals}')