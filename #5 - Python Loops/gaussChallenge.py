# Work out the total of the numbers between 1 and 100, inclusive both 1 and 100.

total = 0
for i in range(1, 101): # The range function generates numbers from 1 to 100 (inclusive).
    total += i # This adds each number to the total variable.
print("The total of the numbers between 1 and 100 is:", total)