guests = ["Albert Einstein", "Jane Austen", "Leonardo da Vinci"]

print(f"Dear {guests[0]},\nI hope this message finds you well. I am writing to cordially invite you to dinner at my "
      f"place.")

print(f"Dear {guests[1]},\nI hope this message finds you well. I am writing to cordially invite you to dinner at my "
      f"place.")

print(f"Dear {guests[2]},\nI hope this message finds you well. I am writing to cordially invite you to dinner at my "
      f"place.")

mid_index = len(guests) // 2

guests.insert(0,"George")
guests.insert(mid_index, "Jake")
guests.append("Luke")

print(f"Dear {guests[0]},\nI hope this message finds you well. I am writing to cordially invite you to dinner at my "
      f"place.")

print(f"Dear {guests[mid_index]},\nI hope this message finds you well. I am writing to cordially invite you to dinner "
      f"at my"f"place.")

print(f"Dear {guests[len(guests)-1]},\nI hope this message finds you well. I am writing to cordially invite you to "
      f"dinner at my"f"place.")

guests.pop()
guests.pop()
guests.pop()
guests.pop()

print(f'this guests : {guests[0]} and {guests[1]} still in the list')
print(f'guests{guests}')

del guests[0]
del guests[0]

print(f'guests: {guests}')