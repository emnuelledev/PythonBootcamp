# This program calculates the total score of a list of student scores.

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
total_score = sum(student_scores) # The sum() function calculates the total of all scores in the list.
largest_score = max(student_scores) # The max() function finds the highest score in the list.
print("The total score of the students is:", total_score)
print("The largest score of the students is:", largest_score)

sum = 0 
for score in student_scores:
    sum += score # This adds each score to the sum variable.
print("The total score of the students is:", sum) # This prints the total score calculated using the for loop.

