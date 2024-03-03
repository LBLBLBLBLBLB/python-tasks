from pathlib import Path
import json

path = Path('number.json')

if path.exists():
    content = path.read_text()
    fav_num = json.loads(content)
    print(f'i know your fav number is {fav_num}')
else:
    number = int(input('enter your number: '))
    content = json.dumps(number)
    path.write_text(content)

    print(f"your fav number {number} has been stored")
