# This game will print Heads or Tails depending on the random number generated. If the random number generated is even, it will print Heads. If the random number generated is odd, it will print Tails.

import random

number = random.randint(1, 100)

if number % 2 == 0:
    print(f"Random number generated: {number}\nHeads")
else:
    print(f"Random number generated: {number}\nTails")
