from pathlib import Path

path = Path('text.txt')
content = path.read_text()

print(content.lower().count('the '))
