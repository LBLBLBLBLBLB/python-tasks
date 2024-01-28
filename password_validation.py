# simple password validator which checks if username and passwords are same
username = input("enter your username: ")
password = input("enter your password: ")

ask_username = input("What is your username?")
ask_password = input("What is your password?")

if username == ask_username and password == ask_password:
    print("welcome")
else:
    print("i dont know you")

