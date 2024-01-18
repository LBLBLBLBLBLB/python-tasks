def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    print(result)
    return result


def collatz_sequence():
    try:
        input_number = int(input("Enter Number"))
        while input_number != 1:
            input_number = collatz(input_number)
    except ValueError:
        print("invalid input, enter integer")


collatz_sequence()
