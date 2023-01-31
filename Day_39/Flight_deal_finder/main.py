#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from notification_manager import NotificationManager
from data_manager import DataManager
from flight_search import FlightSearch

ORIGIN_CITY_IATA_CODE = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

sheet_data = data_manager.get_destination_data()

if sheet_data[0]['iataCode'] == '':
    flight_search = FlightSearch()
    for data in sheet_data:
        data['iataCode'] = flight_search.get_destination_code(data['city'])

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = (datetime.now().date() + timedelta(days=1)).strftime("%d/%m/%Y")
six_month_from_today = (datetime.now().date() + timedelta(days=6 * 30)).strftime("%d/%m/%Y")

for destination in sheet_data:
    flight = FlightSearch().check_flights(
    origin_city_code = ORIGIN_CITY_IATA_CODE,
    destination_city_code=destination["iataCode"],
    from_time=tomorrow,
    to_time=six_month_from_today)

    if flight is not None and \
        flight.price[0] <= sheet_data[0]["lowestPrice"]:
        notification_manager.send_SMS(
            message=f"Low price alert! Only £{flight.price[0]} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
        )