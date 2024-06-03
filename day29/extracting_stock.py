import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

# Initialize an empty DataFrame with the required columns
netflix_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html'

# data  = requests.get(url).text
# print(data)

# Function to fetch data with retry mechanism
def fetch_data(url, retries=5, backoff_factor=0.3):
    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Attempt {i + 1} failed: {e}")
            sleep(backoff_factor * (2 ** i))  # Exponential backoff
    raise Exception(f"Failed to fetch data from {url} after {retries} retries")

# Fetch data
data = fetch_data(url)

# Parse HTML content using BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')

print(soup)

# Extract data and append to DataFrame
for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    Open = col[1].text
    high = col[2].text
    low = col[3].text
    close = col[4].text
    adj_close = col[5].text
    volume = col[6].text

    # Create a new DataFrame for the new row of data
    new_row = pd.DataFrame([{
        "Date": date,
        "Open": Open,
        "High": high,
        "Low": low,
        "Close": close,
        "Adj Close": adj_close,
        "Volume": volume
    }])

    # Append the new data using pd.concat
    netflix_data = pd.concat([netflix_data, new_row], ignore_index=True)

# tep 5: Print the extracted data
# We can now print out the data frame using the head() or tail() function.

# netflix_data.head()

# Now netflix_data contains all the appended rows
print(netflix_data)



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Extracting data using pandas library
# We can also use the pandas read_html function from the pandas library and use the URL for extracting data.

# What is read_html in pandas library?
# pd.read_html(url) is a function provided by the pandas library in Python that is used to extract tables from HTML web pages. It takes in a URL as input and returns a list of all the tables found on the web page.

# read_html_pandas_data = pd.read_html(url)
# # Or you can convert the BeautifulSoup object to a string.

# read_html_pandas_data = pd.read_html(str(soup))
# # Because there is only one table on the page, just take the first table in the returned list.

# netflix_dataframe = read_html_pandas_data[0]
# ​
# netflix_dataframe.head()

