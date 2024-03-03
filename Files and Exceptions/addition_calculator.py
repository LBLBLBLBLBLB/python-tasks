print('Enter two numbers')
print('Enter q to quit')

while True:
    first_num = input('\nEnter first number: ')

    if first_num == 'q':
        break

    second_num = input('\nEnter second number: ')
    if second_num == 'q':
        break

    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        pass
    else:
        print('Sum:', answer)
