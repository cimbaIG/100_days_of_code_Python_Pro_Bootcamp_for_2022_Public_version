student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

""" #Looping through dictionaries
for (key, value) in student_dict.items():
    print(key, value) """

import pandas

student_df = pandas.DataFrame(student_dict)
print(student_df)

""" #Loop through a data frame
for (key, value) in student_df.items():
    print(key, value)
 """
#Loop through rows of a data frame (using iterrows() method)
for (index, row) in student_df.iterrows():
    if row.student == "Angela":
        print(row.score)