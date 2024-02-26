rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil',
    'Yangtze': 'China'
}

for river, country in rivers.items():
    print(f'The {river} runs through {country}')

for river in rivers.keys():
    print(f'river {river}')

for c in rivers.values():
    print(f'country {c}')
