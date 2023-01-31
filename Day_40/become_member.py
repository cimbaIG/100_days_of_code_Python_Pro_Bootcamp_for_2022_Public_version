import requests

SHEETY_ENDPOINT = ""

print("Welcome to Angela's Flight Club.")
print("We find the best flight deals and email you.")
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
repeat_email = input("Type your email again.\n")

if email == repeat_email:

    sheet_inputs = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(SHEETY_ENDPOINT, json=sheet_inputs)
    print(response.text)

    print("You are in the club.")
else:
    print("Email addresses you entered are not the same.")