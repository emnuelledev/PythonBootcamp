# A list is a data structure in Python that is used to store multiple items in a single variable. Lists are ordered, changeable, and allow duplicate values. They are defined by enclosing the items in square brackets [].

# EX 1 
Brazil =["Rio de Janeiro", "São Paulo", "Brasília", "Salvador", "Fortaleza"]
Spain = ["Madrid", "Barcelona", "Valencia", "Seville", "Zaragoza"]
print(f"Brazilian cities: {Brazil}\nSpanish cities: {Spain}")

# We can print the lists by order, like;
print(f"\nThe most known Brazilian city is: {Brazil[0]}\nThe most known Spanish city is: {Spain[0]}")
# We can use negative indexing to print the last item of the list, like;
print(f"\nThe least known Brazilian city is: {Brazil[-1]}\nThe least known Spanish city is: {Spain[-1]}")
# Negative indexing starts from the end of the list, so -1 is the last item, -2 is the second to last item, and so on.
# We cna also edit the list by changing the value of an item in the list, like;
Brazil[0] = "Rio de Janeiro - Edited"
print(f"Rio de Janeiro has been edited to: {Brazil[0]}")
# Add new items to the list using the append() method, like;
Brazil.append("Curitiba")
print(f"\nNew Brazilian city added: {Brazil[-1]}\nThe new list of Brazilian cities is: {Brazil}")

# Theres a hole lot more to learn about lists, but for now, this is enough to get you started with lists in Python. You can find more information about lists in the official Python documentation: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

#  The extend() method is used to add multiple items to the end of a list. It takes an iterable (e.g. another list, tuple, set, etc.) as an argument and adds each item from that iterable to the end of the list. The extend() method modifies the original list in place and does not return a new list.
Brazil.extend(["Recife", "Porto Alegre"])
print(f"\nNew Brazilian cities added: {Brazil[-2:]}\nThe new list of Brazilian cities is: {Brazil}")

# Print the last item of the list using the len() function to get the index of the last item, like;
index = len(Brazil) - 1
print(f"The last Brazilian city is: {Brazil[index]}")

# Print the length of the list using the len() function, like;
ap = len(Spain)
print("The number of Spanish cities in the list is: " + str(ap))

#  Nested Lists
Countries = [Brazil, Spain]
print(f"\nThe list of countries is: {Countries}")

