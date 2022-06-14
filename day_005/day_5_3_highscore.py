"""
You are going to write a program that calculates the highest score from a List of scores.

e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words must match the example. i.e

The highest score in the class is: x
"""

student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

"""
This code will provide the highest score from the list above. 
"""
high_score = 0
for i in student_scores:
    if i > high_score:
        high_score = i
    else:
        continue
print(high_score)