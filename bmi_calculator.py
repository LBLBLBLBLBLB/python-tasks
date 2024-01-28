weight = float(input("enter weight"))
height = float(input("enter height"))

bmi = (weight/height ** 2) * 703

print(f"your bmi is {bmi}")

if bmi > 25:
    print("overweight")
elif bmi < 18.5:
    print("underweight ")
else:
    print("good weight range")
