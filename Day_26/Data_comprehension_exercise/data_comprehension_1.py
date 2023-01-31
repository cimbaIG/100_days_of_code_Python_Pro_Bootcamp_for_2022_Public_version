with open("./Day_26/Data_comprehension_exercise/file1.txt") as file:
    first_list = file.readlines()

with open("./Day_26/Data_comprehension_exercise/file2.txt") as file:
    second_list = file.readlines()

first_list = [int(item) for item in first_list]
second_list = [int(item) for item in second_list]

""" result = []
for item in first_list:
    if item in second_list:
        result.append(item)
 """
# Another option
result = [int(n) for n in first_list if n in second_list]

# Write your code above 👆

print(result)