from pathlib import Path

prompt = input('Enter your name please ')
path = Path('guest.txt')
path.write_text(prompt)
