#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: HW12

import random

#1. Print Hello World!
print("Hello World")
#2. Create three different boolean variables named wifi, login, and admin.
Wifi = random.choice([True, False])
Login = random.choice([True, False])
Admin = random.choice([True, False])

#3. Create a separate integer variable that denotes the number of times
#someone with admin credentials has logged in.
Attempts = 1
#4. Create a nested if statement that checks to see if wifi is true,
#login is true, and admin is true. If they are all true, print a
#welcome message and increase the integer variable by one. If one of them
#is false, print an error message telling them which one they are "missing".
if Wifi == True:
    if Login == True:
        if Admin == True:
            print("-----Welcome home user-----")
            Attempts += 1
        else:
            print("Error: You don't have admin privileges")
    else:
        print("Login details are invalid")
else:
    print("Your Wifi is offline")

print("Attempts:" ,Attempts)
