cities = {
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Tokyo is the most populous city in Japan.'
    },
    'New York': {
        'country': 'USA',
        'population': 8398748,
        'fact': 'New York City is known as "The Big Apple".'
    },
    'London': {
        'country': 'UK',
        'population': 8982000,
        'fact': 'The River Thames flows through London.'
    }
}
for city, city_info in cities.items():
    print(f"\nCity: {city}")
    print(f"\tIn {city_info['country'].title() } lives {city_info['population']}")
    print(f"\tFact about {city_info['country'].title()}: {city_info['fact']}")

# for city, info in cities.items():
#     print(f"\nCity: {city}")
#     for info_k, info_v in info.items():
#         print(f"\t{info_k}: {info_v}")
#     print()
