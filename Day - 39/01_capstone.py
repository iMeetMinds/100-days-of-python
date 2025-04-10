from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

flight_search = FlightSearch()
flight_data = FlightData()

destination_place = input("Where You want to go : ")
destination_code = flight_search.fetch_iata(destination_place)



flight_fetch_data = flight_search.search_flights(destination_code)

lowest_flight_data = flight_data.fetch_lowest_flight_data(flight_fetch_data)

if len(lowest_flight_data) > 0:
    send_noti = NotificationManager()
    send_noti.send_mail(lowest_flight_data[0], destination_place)
    print("Mail Send Successfully!!")