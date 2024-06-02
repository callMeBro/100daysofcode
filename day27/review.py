import pandas as pd

# Define the terms and definitions as lists
terms = [
    "API Key", "APIs", "Audio file", "Authorize", "Beautiful Soup Objects",
    "Bitcoin currency", "Browser", "Candlestick plot", "Client/Wrapper", "CoinGecko API",
    "DELETE Method", "Endpoint", "File extension", "find_all", "GET method",
    "HTML", "HTML Anchor tags", "HTML Tables", "HTML Tag", "HTML Trees",
    "HTTP", "http lib", "Identify", "Instance", "JSON file",
    "Mean value", "Navigable string", "Plotly", "PNG file", "POST method",
    "Post request", "PUT method", "Py-Coin-Gecko", "Python iterable", "Query string",
    "rb mode", "Resource", "Rest API", "Service instance", "Timestamp",
    "Transcribe", "Unix timestamp", "url (Uniform Resource Locator)", "urllib", "Web service",
    "Web scraping", "xlsx", "xml"
]

definitions = [
    "An API key in Python is a secure access token or code used to authenticate and authorize access to an API or web service, enabling the user to make authenticated requests.",
    "APIs (Application Programming Interfaces) are a set of rules and protocols that enable different software applications to communicate and interact, facilitating the exchange of data and functionality.",
    "An audio file is a digital recording or representation of sound, often stored in formats like MP3, WAV, or FLAC, allowing playback and storage of audio content.",
    "In Python, 'authorize' often means granting permission or access to a user or system to perform specific actions or access particular resources, often related to authentication and authorization mechanisms.",
    "Beautiful Soup objects in Python are representations of parsed HTML or XML documents, allowing easy navigation, searching, and manipulation of the document’s elements and data.",
    "Bitcoin is a decentralized digital currency that operates without a central authority, allowing peer-to-peer transactions on a blockchain network.",
    "A browser is a software application that enables users to access and interact with web content, displaying websites and web applications.",
    "A candlestick plot in Python visually represents stock price movements over time, using rectangles to illustrate the open, close, high, and low prices for a given period.",
    "A client or wrapper in Python is a software component that simplifies interaction with external services or APIs, encapsulating communication and providing higher-level functionality for developers.",
    "The CoinGecko API is a web service that provides cryptocurrency market data and information, allowing developers to access real-time and historical data for various cryptocurrencies.",
    "The DELETE method in Python is an HTTP request method used to request the removal or deletion of a resource on a web server.",
    "In Python, an 'endpoint' refers to a specific URL or URI that a web service or API exposes to perform a particular function or access a resource.",
    "A file extension is a suffix added to a filename to indicate the file's format or type, often used by operating systems and applications to determine how to handle the file.",
    "In Python, find_all is a Beautiful Soup method used to search and extract all occurrences of a specified HTML or XML element, returning a list of matching elements.",
    "The GET method in Python is an HTTP request method used to retrieve data from a web server by appending parameters to the URL.",
    "HTML (Hypertext Markup Language) is the standard language for creating and structuring content on web pages, using tags to define the structure and presentation of documents.",
    "HTML anchor tags in Python are used to create hyperlinks within web pages, linking to other web pages or resources using the <a> element with the href attribute.",
    "HTML tables in Python are used to organize and display data in a structured grid format on a web page, constructed with <table>, <tr>, <th>, and <td> elements.",
    "An HTML tag in Python is a specific code enclosed in angle brackets used to define elements within an HTML document, specifying how content should be presented or structured.",
    "HTML trees in Python refer to the hierarchical structure created when parsing an HTML document, representing its elements and their relationships, typically used for manipulation or extraction of data.",
    "HTTP (HyperText Transfer Protocol) is the foundation of data communication on the World Wide Web, used for transmitting and retrieving web content between clients and servers.",
    "A mathematical convention is a fact, name, notation, or usage which is generally agreed upon by mathematicians.",
    "In Python, 'identify' usually means determining if two variables or objects refer to the same memory location, which can be checked using the is operator.",
    "In Python, an 'instance' typically refers to a specific occurrence of an object or class, created from a class blueprint, with its own unique set of data and attributes.",
    "A JSON (JavaScript Object Notation) file is a lightweight data interchange format that stores structured data in a human-readable text format, commonly used for configuration, data exchange, and web APIs.",
    "The mean value in Python is the average of a set of numerical values, calculated by adding all values and dividing by the total number of values.",
    "In Python, a Navigable String is a Beautiful Soup object representing a string within an HTML or XML document, allowing for navigation and manipulation of the text content.",
    "Plotly is a Python library for creating interactive and visually appealing web-based data visualizations and dashboards.",
    "A PNG (Portable Network Graphics) file is a lossless image format in Python that is commonly used for high-quality graphics with support for transparency and compression.",
    "The POST method in Python is an HTTP request method used to send data to a web server, often used for submitting form data and creating or updating resources.",
    "A POST request in Python is an HTTP method used to send data to a web server for the purpose of creating or updating a resource, typically used in web applications and APIs.",
    "The PUT method in Python is an HTTP request method used to update an existing resource on a web server by replacing or modifying it.",
    "Py-Coin-Gecko is a Python library that provides a convenient interface for accessing cryptocurrency data and information from the CoinGecko API.",
    "A Python iterable is an object that can be looped over, typically used in for loops, and includes data structures like lists, tuples, and dictionaries.",
    "A query string in Python is a part of a URL that contains data or parameters to be sent to a web server, typically used in HTTP GET requests to retrieve specific information.",
    "In Python, 'rb' mode is used when opening a file to read it in binary mode, allowing you to read and manipulate non-text files like images or binary data.",
    "In Python, a 'resource' typically refers to an external entity such as a file, database connection, or network object that can be managed and manipulated within a program.",
    "A REST API in Python is a web-based interface that follows the principles of Representational State Transfer (REST), allowing communication and data exchange over HTTP using standard HTTP methods and data formats.",
    "In Python, a 'service instance' typically refers to an instantiated object or entity representing a service, enabling interaction with that service in a program or application.",
    "A timestamp is a representation of a specific moment in time, often expressed as a combination of date and time, used for record-keeping and data tracking.",
    "'Transcribe' typically means converting spoken language or audio into written text, often using automatic speech recognition (ASR) technology.",
    "A UNIX timestamp is a numerical value representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC, used for time-keeping in Unix-based systems and programming.",
    "In Python, a URL (Uniform Resource Locator) is a web address that specifies the location of a resource on the internet, typically consisting of a protocol, domain, and path.",
    "The 'urllib' library in Python is used for working with URLs and making HTTP requests, including functions for fetching web content, handling cookies, and more.",
    "Web services in Python are software components that allow applications to communicate over the internet by sending and receiving data in a standardized format, typically using protocols like HTTP or XML.",
    "Web scraping in Python is the process of extracting data from websites by parsing and analyzing their HTML structure, often done with libraries like BeautifulSoup or Scrapy.",
    "An XLSX file is a file format used for storing spreadsheet data in Excel, containing worksheets, cells, and formulas in a structured manner.",
    "XML (Extensible Markup Language) is a text-based format for storing and structuring data using tags, often used for data interchange and configuration files."
]

#Create a DataFrame
data = {
    "Term": terms,
    "Definition": definitions
}

df = pd.DataFrame(data)

#Display the DataFrame
print(df)

# ave the DataFrame to a CSV file
df.to_csv('terms_and_definitions.csv', index=False)
