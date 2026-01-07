import requests
import os
from datetime import datetime
import json
import time
import logging

# Documentation here: https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll

logs_dir= 'logs'
if os.path.exists(logs_dir):
    pass
else:
    os.mkdir(logs_dir)

filename = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
log_filename = f"logs/api_response_logs_{filename}.log"

logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
)

logger = logging.getLogger()


url = 'https://api.tfl.gov.uk/BikePoint'

number_of_tries = 3
count = 0

while count<number_of_tries:

    response = requests.get(url,timeout=10)
    response_code=response.status_code

    if response.status_code==200:

        json_statham = response.json()

        print(response.status_code)

        # We need to check if the directory exists and make it if not

        dir = 'data'

        if os.path.exists(dir):
            pass
        else:
            os.mkdir(dir)

        file_path = f"{dir}/{filename}.json"

        try:
            with open(file_path, 'w') as file:
                json.dump(json_statham, file)

            print(f'Download successful at {filename} ☘️')
            logger.info(f'Download successful at {filename} ☘️')         
        except Exception as e:
            print(e)
            logger.error(f"An error occurred {e}")

        break

    elif response_code>499 or response_code<200:
        #retry
        print(response.reason)
        time.sleep(10)
        logger.warning(response.reason) 

        count+=1

    else: 
        print(response.reason)
        logger.error(response.reason)
        break


