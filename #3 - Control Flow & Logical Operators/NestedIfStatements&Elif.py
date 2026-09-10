print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? ")) 


if height >= 120:
    print("You can ride the rollercoaster!")
    ticket = 0
    
    age = int(input("What's your age? "))
    if age >= 18:
        ticket = 12
        print("Your ticket is $12.")
    elif age >= 12:
        ticket = 7
        print("Your ticket is $7.")
    else:
        ticket = 5
        print("Your ticket is $5.")
        
    print("Do you want a photo taken? Y or N.")
    photo = input()
    if photo == "Y":
        ticket += 3
        print(f"Your final bill is ${ticket}.")
    else:
        print(f"Your final bill is ${ticket}.")
        
else:
    print("Sorry, you have to grow taller before you can ride.")