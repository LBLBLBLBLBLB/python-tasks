print('Enter two numbers')
print('Enter q to quit')


first_num = input('\nEnter first number: ')
second_num = input('\nEnter second number: ')

try:
    answer = int(first_num) + int(second_num)
except ValueError:
    print('Please enter numbers only.')
else:
    print('Sum:', answer)