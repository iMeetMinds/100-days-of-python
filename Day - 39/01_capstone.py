from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

flight_search = FlightSearch()
flight_data = FlightData()

is_journey_continued = True

while is_journey_continued:
    destination_place = input("Where You want to go : ")
    destination_code = flight_search.fetch_iata_v1(destination_place)

    if destination_code:
        flight_fetch_data = flight_search.search_flights(destination_code)

        lowest_flight_data = flight_data.fetch_lowest_flight_data(flight_fetch_data)

        if lowest_flight_data and len(lowest_flight_data) > 0:
            location_dict = flight_fetch_data['dictionaries']['locations']
            noti_message = flight_data.prepare_noti_msg(lowest_flight_data[0], destination_place, location_dict, flight_search)
            send_noti = NotificationManager()
            send_noti.send_mail(noti_message)

            print("Mail Send Successfully!!")
            is_journey_continued = False
        else:
            print("No cheap flights available as of now. Kindly check later!!")
            is_journey_continued = False
    else:
        print("Invalid Destination. Kindly provide proper destination.")