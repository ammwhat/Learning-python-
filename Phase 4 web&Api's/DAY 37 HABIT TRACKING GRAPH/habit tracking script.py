import requests
import datetime
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "yunganikin"
TOKEN = "qefbalx7z4"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
#response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#print(response.text)
header = {"X-USER-TOKEN":"qefbalx7z4"}
graph_info = {
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
    "id" : "qw2",
    "name" : "coding hours",
    "unit" : "hours",
    "type" : "int",
    "color" : "ajisai"
}
GRAPH_ID = "qw2"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
#graph_response = requests.post(url=GRAPH_ENDPOINT, headers= header, json=graph_info)
#print(graph_response.text)

today = datetime.datetime.now()
formatted_date = today.strftime("%y/%m/%d")
ENTRY_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
entry_info = {
    "date" : formatted_date,
    "quantity" : "2"
}
#entry_response = requests.post(url= ENTRY_ENDPOINT, headers=header, json = entry_info)
#print(entry_response)

UPDATE_ENDPOINT = f"{ENTRY_ENDPOINT}/20260912"
update_info = {
    "quantity" : "5"
}
#update_response = requests.put(url=UPDATE_ENDPOINT, headers=header,  json=update_info)
#print(update_response.text)

delete_repsonse = requests.delete(url = UPDATE_ENDPOINT, headers=header)
print(delete_repsonse.text)

