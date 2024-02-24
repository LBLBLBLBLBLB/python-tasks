multiples_of_three = []

for i in range(3, 31):
    multiples_of_three.append(i*3)

print(multiples_of_three)

mid_index = len(multiples_of_three)//2
print(f'first three items in list are {multiples_of_three[:3]}')
print(f'three items in the middle of the list are {multiples_of_three[mid_index-1:mid_index+2]}')
print(f'last three items in list are {multiples_of_three[-3:]}')