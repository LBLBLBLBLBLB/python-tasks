def make_sandwich(*args):
    print("Making a sandwich with the following ingredients:")
    for ingredient in args:
        print("- " + ingredient)


make_sandwich('a')
make_sandwich('a','b','c','d')
