#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: HW5

#1. Print Hello World!
print("Hello World")
#1. Create a list with 5 strings containing 5 different names in it.
Jacob_List = ["Mack", "John", "Bill", "Tom", "Jake"]
#2. Append a new name onto the Name List.
Jacob_List.append("Jack")
print(Jacob_List)
#3. Print out the 4th name on the list.
print(Jacob_List[3])
#4. Create a list with 4 different integers in it.
Num_List = [42, 38, 1101, 8]
#5. Insert a new integer into the 2nd spot and print the new list.
Num_List.insert(1, 15)
print(Num_List)
#6. Sort the list from lowest to highest and print the sorted list.
Num_List.sort()
print(Num_List)
#7. Add the 1st three numbers on the sorted list together and print the sum.
Addition_Num_List = Num_List[1] + Num_List[2] + Num_List[3]
print(Addition_Num_List)
#8. Create a list with two strings, two variables, and too boolean values.
Jacob_List2 = ["Jefferson", "George", 20, 40, False, True]
#9. Create a print statement that asks the user to input their own index value for the list on #8.
print(Jacob_List2[int(input("Enter index location:"))])