#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: HW16


#1. import the "random" library
import random
#2. print "Hello World!"
print("Hello World!")
#3. Create three variables named a, b, and c, and allow the user to input an integer for each.
a = int(input("[1/3]number: "))
b = int(input("[2/3]number: "))
c = int(input("[3/3]number: "))
#4. Add a and b together, then divide the sum by c. Print the result.
INT = a + b
total_sum = INT / c
print(total_sum)
#5. Round the result from #3 up or down, and then determine if it is even or odd.
M = (round(total_sum))
if M % 2 == 0:
    print("Result:", M, "It's even")
else:
    print("Result:", M, "It's odd")
#6. Create a list of five different random integers between 1 and 10.
Random_List = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
#7. Print the 4th number in the list.
print(Random_List[3])
#8. Append another integer to the end of the list, also random from 1 to 10.
Random_List.append(random.randint(1, 10))
#9. Sort the list from lowest to highest and then print the 4th number in the list again.
Random_List.sort()
print(Random_List[3])
print("__________")
#10. Create a while loop that starts at 1, prints i and then adds i to itself until it is greater than 100.
i = 1
while i <= 100:
    print(i)
    i += i
#11. Create a list containing the names of five other students in the classroom.
Student_List = ["Max", "Austin", "Ethan", "Wyatt", "Jake"]
#12. Create a for loop that individually prints out the names of each student in the list.
for x in Student_List:
    print(x)
#13. Create a for loop that counts from 1 to 100, but ends early if the number is a multiple of 10.
for a in range(1, 101):
    if a % 10 == 0:
        break
    else:
        print(a)

#14. Free space. Do something creative. :)
print("__________")
SL = ["-Max", "-Austin", "-Ethan", "-Wyatt", "-Jake", "-Cruz", "-Santi", "-Anthony"]
random.shuffle(SL)
for x in SL:
    print(x)