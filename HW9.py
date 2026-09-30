#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!
print("Hello World")
#2. Create a dictionary with 3 keys and a value for each key. One of the keys must have a value with a list containing
#three numbers inside.
My_Dictionary = {
    "Brand" : "Nokia",
    "Model" : "3320",
    "Year" : [1992, 2000, 2010]
}
#3. Print the keys of the dictionary from #2.
print(My_Dictionary.keys())
#4. Print the values of the dictionary from #2
print(My_Dictionary.values())
#5. Print one of the three numbers from the list by itself
print(My_Dictionary["Year"][1])
#6. Using the update function, add a fourth key to the dictionary and give it a value.
My_Dictionary.update({"CEO" : "Justin Hotart"})
#7. Print the entire dictionary from #2 with the updated key and value.
print(My_Dictionary)
#8. Make a nested dictionary with three entries containing the name of another classmate and two other pieces of information
#within each entry.
Class_Charactor_List = {
    "Student_1" : {
        "Name" : "Max",
        "HP" : 40,
        "Sport" : False,
    },
    "Student_2" : {
        "Name" : "Wyatt",
        "HP" : 20,
        "Sport" : True,
    },
    "Student_3" : {
        "Name" : "Austin",
        "HP" : 25,
        "Sport" : False,
    },
}
#9. Print the names of all three classmates on the same line.
print(Class_Charactor_List["Student_1"]["Name"], Class_Charactor_List["Student_2"]["Name"], Class_Charactor_List["Student_3"]["Name"])
#10. Use the pop function to remove one of the nested dictionaries inside and print the full dictionary from #8.
Class_Charactor_List.pop("Student_1")
print(Class_Charactor_List)