#----------------STARTER CODE----------------
#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = [0, 1]

#Generates a random integer.
aRandomIndex = randint(0, len(aList)-1)

#---------------- END STARTER CODE----------------
# CHALLENGE 1
# Your generator can create people’s names, business names or
# any other name you choose!

adj = ["Spicy", "Smart", "Quirky", "Majestic", "Cool", "Unique",
     "Tiny", "Comfortable", "Lame", "Supreme", "Pink", "Flimsy"]
adjIndex = randint(0, len(adj)-1)

noun =["Imagination", "Seat Belts", "Computers", "Sand Papers", "Mops", "Refrigerators",
"Politics", "Software", "Receptions", "Planning", "Ladders", "Idea"]
nounIndex = randint(0, len(noun)-1)

randomName = adj[adjIndex] + " " + noun[nounIndex]
print("Your new business is called:", randomName)


# CHALLENGE 2
# You should have lists of multiple courses (e.g. sides, main courses and
# desserts) and randomly create a menu for dinner (one from each category).

mainCourse = ["Mystery Bar", "Mexican", "Salad Bar", "Pizza", "Sushi", "Indian",
                "Sandwich", "Burger Bar", "Steak House"]
mainCourseIndex = randint(0, len(mainCourse)-1)

drink = ["Fountain Drink", "Bottled Drink", "Water", "Cucumber Water"]
drinkIndex = randint(0, len(drink)-1)

dessert = ["Cookie", "Brownie", "Pecan Bar", "Candy", "Protein Bar"]
dessertIndex = randint(0, len(dessert)-1)

print("\nThis is what you're having for lunch:")
print("Main Course: ", mainCourse[mainCourseIndex])
print("Drink: ", drink[drinkIndex])
print("Dessert: ", dessert[dessertIndex])
