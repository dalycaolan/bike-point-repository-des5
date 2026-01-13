from modules.extract import extract_function
from modules.logging import create_log
from datetime import datetime
from modules.load import load
from dotenv import load_dotenv
import os

timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
url = 'https://api.tfl.gov.uk/BikePoint'

extract_logger=create_log('extract',timestamp)

extract_function(url, 3, extract_logger, timestamp)

load_logger=create_log('load', timestamp)

#Load virtual environment

load_dotenv()

# Load in credentials

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET")
BUCKET_NAME=os.getenv("BUCKET_NAME")

# Define path to data folder

current_directory = os.getcwd()
data_folder=os.path.join(current_directory,"data")
print(data_folder)


load(data_folder, AWS_ACCESS_KEY,AWS_SECRET,BUCKET_NAME,load_logger)

