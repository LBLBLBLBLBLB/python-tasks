from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()

print('text file')
print(content)

print('\nprint each line from list')
lines = content.splitlines()
for line in lines:
    print(line)
    