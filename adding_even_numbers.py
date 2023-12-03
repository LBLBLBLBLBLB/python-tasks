# add even numbers from 1 to 100

num_sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        num_sum += i

print("sum of even numbers from 1 to 100:", num_sum)
        