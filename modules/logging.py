import logging
import os
def create_log(prefix, timestamp):
    '''
    Docstring for logging_function

    :param prefix: For the folder name for the logs
    :param timestamp: For the name of the log files
    
    '''
    dir=f'{prefix}_logs'
    os.makedirs(dir,exist_ok=True)

    log_filename = f"{dir}/api_response_logs_{timestamp}.log"

    logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_filename
    )

    return(logging.getLogger())

