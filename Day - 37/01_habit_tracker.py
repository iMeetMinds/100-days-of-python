import requests
from datetime import datetime
import Dummy

PIXELA_END_POINT = 'https://pixe.la/v1/users'

user_data = {
    'token' : Dummy.PIXELA_TOKEN,
    'username' : Dummy.PIXELA_USERNAME,
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

# response = requests.post(url=PIXELA_END_POINT, json=user_data)
# print(response.text)

PIXELA_GRAPH_ENDPOINT = f"{PIXELA_END_POINT}/{Dummy.PIXELA_USERNAME}/graphs"

headers = {
    'X-USER-TOKEN' : Dummy.PIXELA_TOKEN
}
graph_param = {
    'id' : 'graph1',
    'name' : 'Walking Graph',
    'unit' : 'km',
    'type' : 'float',
    'color' : 'momiji'
}

# response = requests.post(url=PIXELA_GRAPH_ENDPOINT, headers=headers, json=graph_param)
# print(response.text)

PIXELA_ADD_PIXEL_ENDPOINT = f"{PIXELA_END_POINT}/{Dummy.PIXELA_USERNAME}/graphs/graph1"

today = datetime.now()

update_graph_data = {
    'date' : today.strftime("%Y%m%d"),
    'quantity' : '5.38'
}
# print(update_graph_data)
# response = requests.post(url=PIXELA_ADD_PIXEL_ENDPOINT, headers=headers, json=update_graph_data)
# print(response.text)

PIXELA_UPDATE_PIXEL_ENDPOINT = f"{PIXELA_END_POINT}/{Dummy.PIXELA_USERNAME}/graphs/graph1/20250408"

today = datetime.now()

update_pixel_data = {
    'quantity' : '4.89'
}
response = requests.put(url=PIXELA_UPDATE_PIXEL_ENDPOINT, headers=headers, json=update_pixel_data)
print(response.text)