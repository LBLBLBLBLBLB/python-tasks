from pathlib import Path

try:
    path_cat = Path('cats.txt')
    path_dog = Path('dogs.txt')

    cat_content = path_cat.read_text()
    dog_content = path_dog.read_text()
except FileNotFoundError:
    print("File not found")
else:
    print(cat_content)
    print(dog_content)