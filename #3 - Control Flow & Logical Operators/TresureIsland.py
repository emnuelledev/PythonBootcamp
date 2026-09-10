print("Welcome to Treasure Island. Your mission is to find the treasure.")

while True:
    left_or_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
    if left_or_right == "right":
        print("You fell into a hole. Game Over.")
        
    elif left_or_right == "left":
        swim_or_wait = input("You come to a lake. There is an island in the middle of the lake.\nType 'wait' to wait for a boat. Type 'swim' to swim across. ")
        if swim_or_wait == "swim":
            print("You get attacked by an angry trout. Game Over.")
            
        elif swim_or_wait == "wait":
            door = input("You arrive at the island unharmed. There is a house with 3 doors.\nOne red, one yellow and one blue. Which colour do you choose?")
            if door == "red":
                print("It's a room full of fire. Game Over.")
                
            elif door == "blue":
                print("Eaten by beasts. Game Over.")
                
            elif door == "yellow":
                print("You found the treasure! You Win!")
                break
            else:
                print("You chose a door that doesn't exist. Game Over.")
                
        else:
            print("You chose an invalid option. Game Over.")
            
    else:
        print("You chose a path that doesn't exist. Game Over.")
        