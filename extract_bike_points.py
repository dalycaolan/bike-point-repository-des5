import requests
import os
from datetime import datetime
import json

# Documentation here: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll

url = 'https://api.tfl.gov.uk/BikePoint'

response = requests.get(url,timeout=10)
json_statham = response.json()

print(response.status_code)

# We need to check if the directory exists and make it if not

dir = 'data'

if os.path.exists(dir):
    pass
else:
    os.mkdir(dir)

filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')

file_path = f"{dir}/{filename}.json"

print(file_path)

with open(file_path, 'w') as file:
    json.dump(json_statham, file)

print(f'Download successful at {filename} ☘️')