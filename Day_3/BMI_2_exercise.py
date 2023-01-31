height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi_index = weight / (height ** 2)

if bmi_index < 18.5:
    print(f"Your BMI is {int(bmi_index)}, you are underweight.")
elif bmi_index < 25:
    print(f"Your BMI is {round(bmi_index)}, you have a normal weight.")
elif bmi_index < 30:
     print(f"Your BMI is {round(bmi_index)}, you are slightly overweight.")
elif bmi_index < 35:
     print(f"Your BMI is {round(bmi_index)}, you are obese.")
else:
     print(f"Your BMI is {round(bmi_index)}, you are clinically obese.")