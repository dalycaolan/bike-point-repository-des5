import logging
import os
import time
import json
import requests

def extract_function(url,number_of_tries,logger,timestamp):
    '''
    Designed for extracting data from bike point API
    
    :param url: Description
    :param number_of_tries: Description
    :param logger: Description
    :param timestamp: Description
    '''

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

            file_path = f"{dir}/{timestamp}.json"

            try:
                with open(file_path, 'w') as file:
                    json.dump(json_statham, file)

                print(f'Download successful at {timestamp} ☘️')
                logger.info(f'Download successful at {timestamp} ☘️')         
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


