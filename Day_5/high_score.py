#Given code
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

""" #My code
for i in range(0,len(student_scores)):
    #print(f"i: student_scores[{i}]: ", student_scores[i])
    for j in range(0,len(student_scores)):
        #print(f"j: student_scores[{j}]: ", student_scores[j])
        if student_scores[j] > student_scores[i]:
            highest_score = student_scores[j]
            #print("highest_score: ",highest_score)

print(f"The highest score in the class is: {highest_score}")
 """
# Easier way
#print(f"The highest score in the class is: {max(student_scores)}")

# Their solution
highest_score = 0
for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)
    
print(f"The highest score in the class is: {highest_score}")