from pathlib import Path

guests = ""

while True:
    name = input('Enter your name please (or type "quit" to exit): ')

    if name.lower() == 'quit':
        break

    guests += name + '\n'

path = Path('guest_book.txt')
path.write_text(guests)