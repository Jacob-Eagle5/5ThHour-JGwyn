#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: SC3

#A common exercise in computer science is "FizzBuzz". The rules of
#the game are simple. Count from 1 to 100 but with every number that
#is divisible by 3 you say "Fizz" instead of the number,
#every number divisible by 5 you say "Buzz" instead,
#and if it's divisible by both you say "FizzBuzz".

#Create a while loop that follows the rules of the game.
H = 0

while H <= 99:
    H += 1
    if H % 3 == 0 and H % 5 == 0:
        print("FizzBuzz")
    elif H % 5 == 0:
        print("Buzz")
    elif H % 3 == 0:
        print("Fizz")
    else:
        print(H)