# Bike Point Extraction Project

Hello, welcome to my bike point extraction project. This project aims to extract a snapshot of data of the bikes around London and any particular time and store them as a JSON file.

## Contents

1. Overview
2. API call
3. Processing Response
4. Error handling and logging

### 1. Overview

We will call a TfL API, documentation on which can be found here:
https://api.tfl.gov.uk/swagger/ui/#!/BikePoint/BikePoint_GetAll

We will set up a robust process of processing the response, depending upon the status of the response coming back to us.

If we receive a good '2XX' response, we will write the JSON output to a data folder and record this success in our logs.

If there is a server-side issue, we will wait 10 seconds and try again, up to three attempts.

If there is a client-side issue, we will end the script and try and debug.

### 2. API call

The url for the API call is the following:

https://api.tfl.gov.uk/BikePoint

By calling this library using a GET command, with our url paramater as above and our timeout parameter set to ten seconds.

### 3. Processing Response

This is where we trifurcate our script.

We set an upper limit of 3 attempts and start our counter at 0. If the response is OK i.e. in the format 2XX, we then ingest the response JSON. We make a data folder if one does not already exist, and write our JSON to this folder with the current datetime inserted into the filename for reference.

If we receive a server-side error, i.e. 1XX or 5XX, we then wait ten seconds and try again and hope for a 2XX response. We add 1 to our counter.

If we receive a client-side error, i.e. 3XX or 4XX, then we end the script and return the reponse reason for this error.

### 4. Error Handling and Logging

Ideally we can account for any potential points of failure for our extraction. Using the logs Python package we can create a log of how our script executes. We create a logs folder if it doesn't already exist, and set up info, warning and error messages where appropriate.
