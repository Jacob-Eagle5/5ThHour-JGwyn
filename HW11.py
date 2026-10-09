#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: HW11

import random
#1. Print "Hello World!"
print("Hello World")
#2. Create a list with three variables that each randomly generate a number between 1 and 100
Num_List = [random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)]
#3. Print the list.
print(Num_List)
#4. Create an if statement that determines which of the three numbers is the highest and prints the result.
if Num_List[0] >= Num_List[1] and Num_List[0] >= Num_List[2]:
    num = Num_List[0]

elif Num_List[1] >= Num_List[0] and Num_List[1] >= Num_List[2]:
    num = Num_List[1]

elif Num_List[2] >= Num_List[1] and Num_List[2] >= Num_List[0]:
    num = Num_List[2]

#5. Tie the result (the largest number) from #4 to a variable called "num".
#Must do the largest Number and call it "num"
print("Largest number:", num)

#6. Create a nested if statement that prints if num is divisible by 2, divisible by 3, both, or neither.

if num % 2 == 0:
    if num % 3 == 0:
        print(f"{num} is divisible both 3 and 2")

    else:
        print(f"{num} is divisible 2")
else:
    if num % 3 == 0:
        print(f"{num} is divisible 3")
    else:
        print(f"{num} is neither")
