#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: HW6


#1. Create a list with 9 different numbers inside.
Numb_List = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#2. Sort the list from highest to lowest.
Numb_List.sort()
print(Numb_List)
#3. Create an empty list.
Emp_List = []
#4. Remove the median number from the first list and add it to the second list.
X = Numb_List.pop(4)
Emp_List.append(X)
#5. Remove the first number from the first list and add it to the second list.
Y = Numb_List.pop(0)
Emp_List.append(Y)
#6. Print both lists.
print(Numb_List, Emp_List)
#7. Add the two numbers in the second list together and print the result.
M = Emp_List[0] + Emp_List[1]
print("Results:", M)
#8. Move the number back to the first list (like you did in #4 and #5 but reversed).
Numb_List.append(M)
#9. Sort the first list from lowest to highest and print it.
Numb_List.sort()
print(Numb_List)