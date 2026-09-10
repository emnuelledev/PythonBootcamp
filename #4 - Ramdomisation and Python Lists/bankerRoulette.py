# This game will decide who pays the bill! :)
import random

friends = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]

# 1st ex
print(f"{random.choice(friends)} is going to buy the meal today!")

# 2nd ex
random_index = random.randint(0, len(friends) - 1)
print(f"{friends[random_index]} is going to buy the meal today!")
