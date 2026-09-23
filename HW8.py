#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: HW8


#1. Import the "random" library
import random
#2. print "Hello World!"
print("Hello World")
#3. Create three different variables that each randomly generate an integer between 1 and 10
Dice_1 = random.randint(1,10)
Dice_2 = random.randint(1, 10)
Dice_3 = random.randint(1, 10)
#4. Print the three variables from #3 on the same line.
print("Rolled:", Dice_1,"|", Dice_2,"|", Dice_3)
#5. Add 2 to the first variable in #3, Subtract 4 from the second variable in #3, and multiply by 1.5 the third variable in #3.
E1 = Dice_1 + 2
E2 = Dice_2 - 4
E3 = Dice_3 * 1.5
#6. Print each result from #5 on the same line.
print("Results:", E1,"|", E2,"|", E3)
#7. Create a list containing four variables that each randomly generate an integer between 1 and 6
Int_List = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
#8. Sort the list in #7 and print it.
Int_List.sort()
print(Int_List)
#9. Add together the highest three numbers in the list from #7 and print the result.
M = Int_List[1] + Int_List[2] + Int_List[3]
print("Results:", M)
#10. Create a list with 5 names of other students in this class and print the list.
Name_List = ["Wyatt", "Austin", "Gavin", "Max", "Cruz"]
print(Name_List)
#11. Shuffle the list in #10 and print the list again.
random.shuffle(Name_List)
print(Name_List)
#12. Print a random choice from the list of names from #10.
print(random.choice(Name_List))