# robo-advisor


##APIKEY: KDAKV7SOOZHAWOBM


#link: https://www.alphavantage.co/query?function=CRYPTO_RATING&symbol=ETH&apikey=KDAKV7SOOZHAWOBM


#URL to request data from: https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&apikey=KDAKV7SOOZHAWOBM



import os
import dotenv import load_dotenv
import requests


#red env variables

load_dotenv()       # 


ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")     


 # read frm .env file





#make a request

import requests

symbol = "MSFT"   # ask for user input instead of hardcoding

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}"

response = requests.et(request_url)
print(type(response))
print(response.text)