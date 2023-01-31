from pprint import pprint
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = ""
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    
    def get_destination_code(self, city_name):
        header = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "term": city_name,
            "location_types": "city" 
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=params, headers=header)
        response.raise_for_status()
        result = response.json()['locations'][0]['code']
        return result
    
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        header = {
            "apikey": TEQUILA_API_KEY
        }
        params = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time,
            "date_to": to_time,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers=header)
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data['price'],
            origin_city=data['route'][0]['cityFrom'],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]            
        )

        print(f"{flight_data.destination_city}: £{flight_data.price[0]}")
        return flight_data