with open("./Day_24/Mail_merge_project/Input/Names/invited_names.txt", "r") as file:
    invited_names = file.readlines()

with open("./Day_24/Mail_merge_project/Input/Letters/starting_letter.txt", "r") as file:
    letter_lines = file.readlines()

first_line = letter_lines[0]
new_letter_lines = letter_lines
for name in invited_names:
    stripped_name = name.strip()
    new_letter_lines[0] = first_line.replace("[name]", f"{stripped_name}")
    file = open(f"./Day_24/Mail_merge_project/Output/ReadyToSend/letter_for_{name}", "w")
    for line in new_letter_lines:
        file.write(line)
    file.close()
    new_letter_lines[0] = first_line