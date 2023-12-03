print("Welcome to Treasure Island")
print("Your mission is to find the Treasure.")
direction = input("You\'re at a cross road. Where do you want to go? Type \"left\" or \"right\": ")
if direction == "left":
    choice = input("You've come to lake.There is island in the middel if the lake. Type \"wait\" or \"swim\" ")
    if choice == "wait":
        door = input("Which door : Red, blue, yellow ")
        if door == "yellow":
            print("You Win!")
        elif door == "Blue":
            print("Eaten by beasts ")
        elif door == "red":
            print("Burned ny fire. Game over.")
    else:
        print("You get attacked by an angry trout. Game over")
else:
    print("You fell into a hole. Game Over")