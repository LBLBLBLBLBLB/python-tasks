favorite_places = {
    'Alice': ['Paris', 'New York'],
    'Bob': ['London'],
    'Charlie': ['Tokyo', 'Sydney', 'Rome']
}

print(favorite_places)

for name_k, place_val in favorite_places.items():
    print(f"{name_k}'s favorite places: ")
    for place in place_val:
        print(f'{place}')
    print()