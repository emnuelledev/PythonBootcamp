import random 
import my_module

# Will generate a random number between 1 and 100
numbers = random.randint(1, 100)
print(f"Random number generated: {numbers}")

# Printing the favorite color from the my_module
print(f"\nMy favorite color is: {my_module.fav_color}\nThis is a print statement from the my_module.py file.")

# Float numbers can also be generated using the random module. The following code will generate a random float number between 0 and 1:
random_float = random.random()
print(f"\nRandom float generated: {random_float}\nThis is a print statement from the random.random() module.\n 0.0 <= random.random() < 1.0 \nThis is a float number between 0 and 1.")

# Float numbers can also be generated between 0 and 10 by multiplying the random.random() function by 10. The following code will generate a random float number between 0 and 10:
random_float_x = random.random() * 10
print(f"\nRandom float generated: {random_float_x}\nThis is a print statement from the random.random() module multiplied by 10.\nMind you to always keep in mind that the random.random() function generates a float number\nbetween 0 and 1, so if you want to generate a float number between 0 and 10,\nyou need to multiply it by 10.")

# Float numbers can also be generated between 1 and 10 using the random.uniform() function. The following code will generate a random float number between 1 and 10:
random_uniform = random.uniform(1, 10)
print(f"\nRandom float generated: {random_uniform}\nThis is a print statement from the random.uniform() module.\nThis is a float number between 1 and 10.")
# It almost does the same thing as the random.random() function, the only difference is it's not entirely sure depending on rounding, whether if you will get 10 or not in the random_float.




