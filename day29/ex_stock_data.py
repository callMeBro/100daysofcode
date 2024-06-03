# # Extracting Stock Data Using a Python Library
# # A company's stock share is a piece of the company more precisely:

# # A stock (also known as equity) is a security that represents the ownership of a fraction of a corporation. This entitles the owner of the stock to a proportion of the corporation's assets and profits equal to how much stock they own. Units of stock are called "shares." [1]

# # An investor can buy a stock and sell it later. If the stock price increases, the investor profits, If it decreases,the investor with incur a loss.  Determining the stock price is complex; it depends on the number of outstanding shares, the size of the company's future profits, and much more. People trade stocks throughout the day the stock ticker is a report of the price of a certain stock, updated continuously throughout the trading session by the various stock market exchanges.

# # You are a data scientist working for a hedge fund; it's your job to determine any suspicious stock activity. In this lab you will extract stock data using a Python library. We will use the yfinance library, it allows us to extract data for stocks returning data in a pandas dataframe. You will use the lab to extract.


# import yfinance as yf
# import pandas as pd

# # Using the Ticker module we can create an object that will allow us to access functions to extract data. To do this we need to provide the ticker symbol for the stock, here the company is Apple and the ticker symbol is AAPL.
# apple = yf.Ticker("AAPL")


# # wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json


# import json

# # Using the attribute info we can extract information about the stock as a Python dictionary
# with open('apple.json') as json_file:
#     apple_info = json.load(json_file)
#     # Print the type of data variable    
#     print("Type:", type(apple_info))
# print(apple_info)

# # get the 'country' using the key country
# apple_info['country']


# # EXTRACTING A SHARE
# # A share is the single smallest part of a company's stock  that you can buy, the prices of these shares fluctuate over time. Using the <code>history()</code> method we can get the share price of the stock over a certain period of time. Using the `period` parameter we can set how 
# # far back from the present to get data. The options for `period` are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
# apple_share_price_data = apple.history(period="max")


# # The format that the data is returned in is a Pandas DataFrame. With the Date as the index the share Open, High, Low, Close, Volume, and Stock Splits are given for each day.
# apple_share_price_data.head()


# # We can reset the index of the DataFrame with the reset_index function. We also set the inplace paramter to True so the change takes place to the DataFrame itself
# apple_share_price_data.reset_index(inplace=True)


# # plot the Open price against the Date
# apple_share_price_data.plot(x="Date", y="Open")


# # Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount of money returned per share an investor owns. Using the variable dividends we can get a dataframe of the data. 
# # The period of the data is given by the period defined in the 'history` function.
# apple.dividends


# # We can plot the dividends overtime:
# apple.dividends.plot()


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# EXERCISE 

# import yfinance as yf
# import pandas as pd
# amd = yf.Ticker("AMD")


# import json
# with open('amd.json') as json_file:
#     amd_info = json.load(json_file)
#     # Print the type of data variable    
#     #print("Type:", type(apple_info))
# print(amd_info)



# print(amd_info['country'])



# amd_price_data = amd.history(period="max")


# # Check if data is available
# if not amd_price_data.empty:
#     # Access the first day's volume data
#     first_day_volume = amd_price_data.iloc[0]['Volume']
#     print("First day's volume:", first_day_volume)
# else:
#     print("No historical price data available for AMD")

# first_day_volume = amd_price_data.iloc[0]['Volume']


# print(first_day_volume)


import yfinance as yf
import pandas as pd
import json

# Load AMD company information from JSON file
with open('amd.json') as json_file:
    amd_info = json.load(json_file)

# Print the loaded data
print(amd_info)

# Access specific information (e.g., country)
print(amd_info['country'])

# Retrieve historical stock price data for AMD
amd = yf.Ticker("AMD")
amd_price_data = amd.history(period="max")

