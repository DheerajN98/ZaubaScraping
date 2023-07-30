# Web Scraping Zaubacorp and Storing Data in MongoDB

![MongoDB](https://img.shields.io/badge/MongoDB-v6.0.0-green)

This repository contains a Python script that performs web scraping on the website "Zaubacorp" to extract company data and store it in a MongoDB database. The script uses the requests library to send HTTP requests to the website, lxml for parsing the HTML response, and pymongo to connect to and interact with the MongoDB database.


## Installation and Setup

Before running the script, you need to have the following installed:

Python: Make sure you have Python installed on your system. You can download it from the official Python website: https://www.python.org/downloads/

MongoDB: You need to have a MongoDB server set up or use a cloud-hosted MongoDB service like MongoDB Atlas: https://www.mongodb.com/cloud/atlas

<h2>Configuration:</h2>
Before running the script, you need to configure the MongoDB connection URL and provide your MongoDB cluster credentials. Modify the CONNECTION_URL variable in the 
script to match your MongoDB connection URL: 

CONNECTION_URL = "mongodb+srv://USERNAME:PASSWORD@<CLUSTER_URL>/test?retryWrites=true&w=majority"

Replace USERNAME, PASSWORD, and <CLUSTER_URL> with your actual MongoDB credentials and cluster URL.

To start the web scraping process, execute the Python script:
python zaubacorp_scraper.py

The script will start scraping the company data from the Zaubacorp website and store it in the specified MongoDB database. The scraped data will be inserted into the "Companies" collection within the "ZaubaCorp" database.

<h2>Script Details</h2>
<ul>
  <li><b>useragentselector() function:</b> This function randomly selects a user agent from a list to be used as the request header. It helps in mimicking different browsers and avoiding detection.</li>
  <li><b>crawl(produrl, collection) function:</b> This function performs the web scraping on the specified produrl, which is the URL of the Zaubacorp website to scrape. The scraped data is then inserted into the MongoDB collection.</li>
</ul>

<h2>MongoDB Connection</h2>
The script establishes a connection to the MongoDB server using the provided CONNECTION_URL and creates a connection to the "ZaubaCorp" database. It then accesses the "Companies" collection within the database, where the scraped data will be stored.

<h2>Error Handling</h2>
The script includes error handling to handle various exceptions that may occur during the web scraping process. It handles exceptions related to HTTP requests, HTML parsing, and data extraction. If an error occurs, the script prints a relevant error message to the console.


## Contact

If you want to contact me, you can reach me through below handles.

[![gmail](https://img.shields.io/badge/Dheeraj_Nair-FF0000?style=for-the-badge&logo=gmail&logoColor=white&labelColor=FF0000)](dheerajnair98@gmail.com)

[![GitHub](https://img.shields.io/badge/Dheeraj_Nair-20232A?style=for-the-badge&logo=Github&logoColor=white)](https://github.com/DheerajN98)

© 2023 Dheeraj_Nair
