#Name: Jacob Gwyn
#Class: 5th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

num_of_players = int(input("Give me a number of players:"))
TS = 0

for i in range(1, num_of_players):
    rating = int(input("Rating 1 to 5:"))

    while rating < 1 or rating > 5:
        rating = int(input("Please give a valid 1 to 5:"))
    else:
        TS += rating

avg_rating = TS/(num_of_players - 1)
print("Average Score:", avg_rating)