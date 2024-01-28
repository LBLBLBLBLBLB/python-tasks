user_input = input(
    """Press C to convert from Fahrenheit to Celsius:
Press F to convert from Celsius to Fahrenheit: """
)

if user_input.upper() == 'C':
    print("your choice is C")
    F = int(input("Please enter the temperature in Fahrenheit:"))
    C = (F - 32) * 5 / 9
    print(f"The temperature in Celsius is {C}")
else:
    print("your choice is F")
    C = int(input("Please enter the temperature in Fahrenheit:"))
    F = int((C * 9/5) + 32)
    print(f"The temperature in Celsius is {F}")
