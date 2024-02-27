message = 'Enter your age (type quit to exit)'


while True:
    age = input(message)
    if age == 'quit':
        break
    elif int(age) < 3:
        print('message is free')
    elif 3 <= int(age) < 12:
        print('ticket price is 10 usd')
    else:
        print('ticket is 15 usd')