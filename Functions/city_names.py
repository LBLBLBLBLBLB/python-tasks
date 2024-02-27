def city_country(city,country):
    formatted = f'{city} {country}'
    return formatted.title()


print(city_country('tbilisi', 'georgia'))

country1 = city_country('germany', 'berlin')
print(country1)