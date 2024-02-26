pet1 = {'kind': 'dog', 'owner': 'Alice'}
pet2 = {'kind': 'cat', 'owner': 'Bob'}
pet3 = {'kind': 'parrot', 'owner': 'Charlie'}
pet4 = {'kind': 'rabbit', 'owner': 'David'}

pets = [pet1, pet2, pet3, pet4]


for pet in pets:
    for pet_key, pet_info in pet.items():
        print(f'{pet_key.title()}: {pet_info}')
    print("")