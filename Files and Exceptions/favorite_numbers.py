from pathlib import Path
import json

path = Path('number.json')
number = int(input('Enter your favorite number'))

content = json.dumps(number)
path.write_text(content)

content_to_read = path.read_text()
favorite_number = json.loads(content_to_read)
print(f"I know your favorite number! It’s {favorite_number}.")