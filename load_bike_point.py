import boto3
from dotenv import load_dotenv
import os

load_dotenv()

# Load in credentials

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET = os.getenv("AWS_SECRET")
BUCKET_NAME=os.getenv("BUCKET_NAME")

# Define path to data folder

current_directory = os.getcwd()
data_folder=os.path.join(current_directory,"data")
print(data_folder)

# Create list of jsons

list_of_files=os.listdir(data_folder)
upload_files=[]
for file in list_of_files:
    is_json=file.endswith(".json")
    if is_json:
        upload_files.append(file)

print(upload_files)

if len(upload_files)==0:
    print("Error: List is empty")
else:

    for json in upload_files:
        json_folder=os.path.join(data_folder,json)
        print(json_folder)
        s3_client = boto3.client(
            's3'
            ,aws_access_key_id = AWS_ACCESS_KEY
            ,aws_secret_access_key = AWS_SECRET
            )
        try:
            s3_client.upload_file(json_folder,BUCKET_NAME,json)
        except boto3.ClientError as e:
            print(f"An exception occurred: {e}")