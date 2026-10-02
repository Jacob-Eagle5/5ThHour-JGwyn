#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: Scenario 1

#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead has asked you
#to create a nested dictionary containing five enemy creatures (and their properties)
#for combat testing. Additionally, the testers are asking for a way to input changes
#to the enemy's damage values for balancing, as well as having it print those changes
#to confirm they went through.

#Other than damage which is required, it is up to you to decide what properties are
#important and the theme of the game.

Enemy_List = {
    "Enemy_1" : {
        "Enemy Type" : "Corrupt Villager",
        "HP" : 10,
        "Dmg" : 2,
    },
    "Enemy_2" : {
        "Enemy Type" : "Corrupt Iron-Golem",
        "HP" : 20,
        "Dmg" : 11,
    },
    "Enemy_3" : {
        "Enemy Type" : "Wizard",
        "HP" : 30,
        "Dmg" : 18,
    },
    "Enemy_4" : {
        "Enemy Type" : "Ender Dragon's Guardian",
        "HP" : 50,
        "Dmg" : 25,
    },
    "Enemy_5" : {
        "Enemy Type" : "Ender Dragon",
        "HP" : 100,
        "Dmg" : 50,},
}
#Enemy's DMG Testing
print("Corrupt Villager DMG:" ,Enemy_List["Enemy_1"]["Dmg"])
print("Corrupt Iron-Golem DMG:",Enemy_List["Enemy_2"]["Dmg"])
print("Wizard DMG:" ,Enemy_List["Enemy_3"]["Dmg"])
print("Ender Dragon's Guardian DMG:" ,Enemy_List["Enemy_4"]["Dmg"])
print("Ender Dragon DMG:" ,Enemy_List["Enemy_5"]["Dmg"])

print("------------------------------------------------")

#Modify Enemy's Values
Enemy_List["Enemy_1"].update({"Dmg" : int(input("Change DMG value of Corrupt Villager:"))})
Enemy_List["Enemy_2"].update({"Dmg" : int(input("Change DMG value of Corrupt Iron-Golem:"))})
Enemy_List["Enemy_3"].update({"Dmg" : int(input("Change DMG value: of Wizard:"))})
Enemy_List["Enemy_4"].update({"Dmg" : int(input("Change DMG value of Ender Dragon's Guardian:"))})
Enemy_List["Enemy_5"].update({"Dmg" : int(input("Change DMG value of Ender Dragon:"))})

print("------------------------------------------------")

print( "Corrupt Villager DMG:", Enemy_List["Enemy_1"]["Dmg"])
print( "Corrupt Iron-Golem DMG:", Enemy_List["Enemy_2"]["Dmg"])
print( "Wizard DMG:", Enemy_List["Enemy_3"]["Dmg"])
print( "Ender Dragon's Guardian DMG:", Enemy_List["Enemy_4"]["Dmg"])
print( "Ender Dragon DMG:", Enemy_List["Enemy_5"]["Dmg"])