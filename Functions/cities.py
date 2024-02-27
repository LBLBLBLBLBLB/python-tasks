def describe_cities(name, country='Georgia'):
    print(f'{name.title()} is in {country.title()}')


describe_cities("Tbilisi")
describe_cities("Tokyo", "Japan")
describe_cities("Paris", "France")