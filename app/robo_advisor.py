print("TODO: make a web request for some stock")



#import os
##import dotenv import load_dotenv
import requests


#red env variables

#load_dotenv()       # 


##ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")     


 # read frm .env file



#make a request

#import requests

#symbol = "MSFT"   # ask for user input instead of hardcoding

#request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

#response = requests.et(request_url)
#print(type(response))
##print(response.text)


import os
from dotenv import load_dotenv
import requests
load_dotenv() # go get env vars from the .env file
# read env variables
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
# make a request
symbol = "MSFT" # ask for a user input
request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"
response = requests.get(request_url)
print(type(response))
print(response.text)