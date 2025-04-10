
class FlightData:

    def __init__(self):
        self.lowest_flight_data = ""


    def fetch_lowest_flight_data(self, flight_data):
        data = flight_data['data']
        lowest_price = float(725)
        for n_dict in data:
            if float(n_dict['price']['total']) <= float(lowest_price):
                lowest_price = float(n_dict['price']['total'])

        return [n_dict for n_dict in data if float(n_dict['price']['total']) == float(lowest_price)]