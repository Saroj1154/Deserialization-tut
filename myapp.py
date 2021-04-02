import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

#data to be sent to inserted
data = {
    'name': 'Saroj',
    'roll': 102,
    'city': 'Bhaktapur', 
}

#converting this data into json format using dumps method
json_data = json.dumps(data) 

#Sending this json data as a post request to a url endpoint
r = requests.post(url= URL, data= json_data)

data = r.json()
print(data) 