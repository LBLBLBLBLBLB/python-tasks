people = {
           'person1': {'first_name': 'George', 'last_name': 'Lucas', 'age': 30, 'city': 'Washington'},
           'person2': {'first_name': 'Tyler', 'last_name': 'Durden', 'age': 40, 'city': 'New York'},
           'person3': {'first_name': 'Jimmie', 'last_name': 'Page', 'age': 60, 'city': 'London'}
          }

for person_k, person_v in people.items():
    print(f'person key: {person_k}')
    for key,val in person_v.items():
        print(f'{key.title()}: {val}')
    print()
 