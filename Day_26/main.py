""" # List comprehension
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

range_list = range(1,5)
double_range_list = [num*2 for num in range_list]
print(double_range_list)

# Conditional list comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
upper_case_names = [name.upper() for name in names if len(name) > 5]
print(upper_case_names) """

from random import randint


names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

#dict_comprehension = {new_key:new_value for item in list}
#dict_comprehension = {new_key:new_value for (key,value) in dict.items() if test}
#Working with dictionary: dict = {new_key:new_value for (key, value) in dict.items()} 

student_scores = {student:randint(0,100) for student in names}
print(student_scores)
passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
print(passed_students)