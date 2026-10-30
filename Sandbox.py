import math, random
print("=====================================================================================")
print("Crazy Py Calculator")
print("-----------------------------------------------------------------------")
num1 = int(input("Give me a number:"))
print("-----------------------------------------------------------------------")
num2 = int(input("Give me another number:"))
print("-----------------------------------------------------------------------")
Action = str(input("Do you like to do +, -, *, /, **(squared), Pi, coinflip, Boss HP Flex:"))
print("-----------------------------------------------------------------------")
if Action == "+":
    print("Results:", num1 + num2)
elif Action == "-":
    print("Results:", num1 - num2)
elif Action == "*":
    print("Results:", num1 * num2)
elif Action == "/":
    print("Results:", num1 / num2)
elif Action == "**":
    print("Results:", num1 ** num2)
elif Action == "Pi":
    PieMath = math.pi * (num1 + num2)
    print("Results:", PieMath)
elif Action == "coinflip":
    coinflip = random.randint(0, 1)
    if coinflip == 1:
        print("Heads")
    else:
        print("Tails")
elif Action == "Boss HP Flex":
    player_HP = int(input("Your HP is:"))
    Boss_HP = random.randint(1, 999)
    if player_HP > Boss_HP:
        print("Your HP is greater than Boss HP")
    else:
        print("Your boss HP is greater than your HP")

else:
    print("Invalid Action")