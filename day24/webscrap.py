import requests
from bs4 import BeautifulSoup
from requests.exceptions import RequestException, Timeout


# Specify the URL of the webpage you want to scrape
url = 'https://www.udemy.com/'

# # Function to fetch webpage content with User-Agent header
# def fetch_webpage(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'
#     }
#     try:
#         print("Sending request to URL...")
#         response = requests.get(url, headers=headers, timeout=10)
#         response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
#         print("Request successful.")
#         return response.text
#     except ConnectionError as e:
#         print(f"Connection error: {e}")
#     except Timeout as e:
#         print(f"Request timed out: {e}")
#     except RequestException as e:
#         print(f"An error occurred: {e}")
#     return None

# # Fetch the webpage content
# html_content = fetch_webpage(url)

# if html_content:
#     # Create a BeautifulSoup object to parse the HTML
#     soup = BeautifulSoup(html_content, 'html.parser')

#     # Display a snippet of the HTML content to ensure we fetched it correctly
#     print("HTML Snippet:", html_content[:500])

#     # Find all <a> tags (anchor tags) in the HTML
#     links = soup.find_all('a')

#     # Iterate through the list of links and print their text
#     for link in links:
#         # Get the text of the <a> tag
#         link_text = link.text.strip()  # Using strip() to remove leading/trailing whitespace
#         if link_text:  # Only print non-empty text
#             print("Anchor text:", link_text)
# else:
#     print("Failed to fetch the webpage content.")







# Send an HTTP GET request to the webpage
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Store the HTML content in a variable
    html_content = response.text

    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Display a snippet of the HTML content to ensure we fetched it correctly
    print("HTML Snippet:", html_content[:500])

    # Find all <a> tags (anchor tags) in the HTML
    links = soup.find_all('a')

    # Iterate through the list of links and print their text
    for link in links:
        # Get the text of the <a> tag
        link_text = link.text.strip()  # Using strip() to remove leading/trailing whitespace
        if link_text:  # Only print non-empty text
            print("Anchor text:", link_text)
else:
    print(f"Failed to fetch the webpage. Status code: {response.status_code}")
