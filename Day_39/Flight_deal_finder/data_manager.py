import requests

SHEETY_API_KEY = ""

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        self.response = requests.get(url=SHEETY_API_KEY)
        self.results = self.response.json()
        return self.results['prices']

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_API_KEY}/{city['id']}", json=new_data)
            print(response.text)