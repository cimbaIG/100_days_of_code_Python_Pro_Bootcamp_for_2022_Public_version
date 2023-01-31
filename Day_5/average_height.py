student_heights = input("Input a list of student heights ").split()
avg_height = 0
tot_stud_num = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

for n in student_heights:
    tot_stud_num += 1

for height in student_heights:
    avg_height += height / tot_stud_num

round_avg_height = round(avg_height)
print(round_avg_height)

# My solution
""" for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    avg_height += student_heights[n] / len(student_heights)

round_avg_height = round(avg_height)
print(round_avg_height)
 """ 