import os
import boto3

def load(data_dir,access_key,access_secret,bucket_name,logger):
    '''
    Docstring for load
    
    :param data_dir: Where we will pull data from
    :param access_key: AWS access key from .env
    :param access_secret: AWS secret from .env
    :param bucket_name: Name of our S3 bucket, destination for data load
    :param logger: using logger in function to make load logs
    '''
    # Create list of jsons

    list_of_files=os.listdir(data_dir)
    upload_files=[]
    for file in list_of_files:
        is_json=file.endswith(".json")
        if is_json:
            upload_files.append(file)

    print(upload_files)

    # Check jsons exist

    if len(upload_files)==0:
        print("Error: List is empty")
        logger.error('No files to upload >.<')
    else:

        # For each json, upload to s3 bucket

        for json in upload_files:
            json_folder=os.path.join(data_dir,json)
            print(json_folder)
            s3_client = boto3.client(
                's3'
                ,aws_access_key_id = access_key
                ,aws_secret_access_key = access_secret
                )
            
            # Make attempt to upload

            try:
                s3_client.upload_file(json_folder,bucket_name,json)
                logger.info(f'{json} uploaded successfully')
                os.remove(json_folder)
                logger.info(f'{json} removed')

            except boto3.ClientError as e:
                print(f"An exception occurred: {e}")
