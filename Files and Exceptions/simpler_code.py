from pathlib import Path

path = Path('learning_python.txt')
content = path.read_text()

for line in content.splitlines():
    line = line.replace('Python', 'C')
    print(line)
