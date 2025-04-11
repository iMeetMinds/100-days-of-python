from flight_search import FlightSearch
import constants as const

class FlightData:

    def __init__(self):
        self.lowest_flight_data = ""

    def fetch_lowest_flight_data(self, flight_data):
        data = flight_data['data']
        if len(data) > 0:
            lowest_price = float(10000)
            for n_dict in data:
                if float(n_dict['price']['total']) <= float(lowest_price):
                    lowest_price = float(n_dict['price']['total'])

            return [n_dict for n_dict in data if float(n_dict['price']['total']) == float(lowest_price)]
        else:
            return None

    def prepare_noti_msg(self,flight_data, destination_place, location_dict, fs:FlightSearch):
        segments = flight_data['itineraries'][0]['segments']

        total_price = flight_data['price']['total']
        departure_iata_code = segments[0]['departure']['iataCode']
        destination_iata_code = segments[-1]['arrival']['iataCode']
        departure_time = segments[0]['departure']['at']
        destination_time = segments[-1]['arrival']['at']

        email_content = (f"Low Price Alert!! \n\n Only ${total_price} to fly from "
                         f"{const.CURRENT_PLACE}-{departure_iata_code}"
                         f" to {destination_place}-{destination_iata_code}"
                         f", from {departure_time} to {destination_time}")

        if len(segments) > 0:
            departure_codes = [n['departure']['iataCode'] for n in segments if n['departure']['iataCode'] != departure_iata_code]
            arrival_codes = [n['arrival']['iataCode'] for n in segments if n['arrival']['iataCode'] != destination_iata_code]

            all_stop_iata_codes = list(dict.fromkeys(departure_codes + arrival_codes))
            stop_name = []
            for iata_code in all_stop_iata_codes:
                city_code = location_dict[iata_code]['cityCode']
                country_code = location_dict[iata_code]['countryCode']
                # stop_name += fs.fetch_city_name(city_code, country_code)
                stop_name.append(f"{fs.fetch_country_name(country_code)}-{city_code}")

            email_content += f"\n\n Flight has {len(all_stop_iata_codes)} stop, via {', '.join(stop_name)}."

        return email_content

