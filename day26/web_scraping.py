# BeautifulSoup: BeautifulSoup is a Python library used for web scraping purposes to pull the data out of HTML and XML files. It creates a parse tree from page source code that can be used to extract data in a hierarchical and more readable manner.
from bs4 import BeautifulSoup            
#Selenium: Selenium is a tool used for controlling web browsers through programs and automating browser tasks.
from selenium import webdriver
import requests
# Scrapy: Scrapy is an open-source and collaborative web crawling framework for Python. It is used to extract the data from the website
import scrapy
import pandas as pd


URL = "http://www.example.com"
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


# class inherets from scrapy.spider  
class QuotesSpider(scrapy.Spider):
    # name for spider
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com/tag/humor/',]
    #callback method that scrappy calls wheever it recieves a response for the request
    def parse(self, response):
        #  select all elements with a class quote within the responce object
        for quote in response.css('div.quote'):
              yield {'quote': quote.css('span.text::text').get()}             #the code extracts the text of the quote using another CSS selector (span.text::text). It then yields a dictionary containing the extracted quote text. The yield statement makes this a generator function, allowing Scrapy to process the extracted data asynchronously.
            



# driver = webdriver.Firefox(): This line creates an instance of the Firefox WebDriver, which allows Python to control the Firefox browser. When you execute this line, Selenium will attempt to open a new instance of the Firefox browser. If you haven't already, you'll need to have the geckodriver executable in your system PATH or specify its location explicitly using executable_path parameter. The WebDriver facilitates communication between your Python script and the browser.
# driver.get("http://www.example.com"): This line instructs the WebDriver to navigate to the specified URL, in this case, "http://www.example.com". Once the browser opens, it will load the content of this webpage. This method blocks until the page is fully loaded.
driver = webdriver.Firefox()
driver.get("http://www.example.com")            




URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'


# extract the required table as a dataframe 
URL = 'https://en.wikipedia.org/wiki/List_of_largest_banks'
tables = pd.read_html(URL)
df = tables[0]
print(df)


URL = 'https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)'
tables = pd.read_html(URL)
df = tables(2) # the required table will have index 2
print(df)
# Copied!
# The output of the print s