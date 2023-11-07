#!/usr/bin/python3
import requests
import pandas as pd

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    ## first grab credentials
    nasacreds = returncreds()


    user_start = input("Please enter a start date in the following format: YYYY-MM-DD")
    ## update the date below, if you like
    startdate = f"start_date={user_start}"

    user_end = input("Please enter an end date in the following format: YYYY-MM-DD [default is todays date]")

    enddate = ""

    if user_end:
        enddate = f"end_date={user_end}"


    full_url = NEOURL + startdate + "&" + nasacreds
    if enddate:
        full_url += "&" + enddate
    # make a request with the request library
    neowrequest = requests.get(full_url)

    # strip off json attachment from our response
    neodata = neowrequest.json()
    
    test_df = pd.read_json(neowrequest.json())
    print(test_df)

    ## display NASAs NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

