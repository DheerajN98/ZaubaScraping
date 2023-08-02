import HTMLParser
import time
import random
import math
import requests
from lxml import html
import pymongo


def useragentselector():
    """Function to randomly select a user agent for request headers"""
    user_agent = [
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v2183974942390436904 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v1149670349770359751 t5560511831922518437 ath259cea6f altpriv cvcv=2 smf=0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v9688968893 t5504877869796311411 athfa3c3975 altpub cvcv=2 smf=0 svfu=1',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v3806700650136064627 t8116704791844188491 ath5ee645e0 altpriv cvcv=2 smf=0 svfu=1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v5254709137072837719 t196484837431047734 ath1fb31b7a altpriv cvcv=2 smf=0 svfu=1',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3285141929 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v7416116440408545761 t4763100215355965436 ath259cea6f altpriv cvcv=2 smf=0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v6876771777591115601 t8360729428027585528 ath259cea6f altpriv cvcv=2 smf=0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3285144570 t6006063806750198674 athfa3c3975 altpub cvcv=2 smf=0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v1769854044280605105 t5747064355914000718 ath259cea6f altpriv cvcv=2 smf=0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 RuxitSynthetic/1.0 v9087459017265711609 t6488874039671701825 ath5ee645e0 altpriv cvcv=2 smf=0 svfu=1',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3285153285 t3984374008602804876 athfa3c3975 altpub cvcv=2 smf=0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v1148457910886626022 t2805780631004553331 ath5ee645e0 altpriv cvcv=2 smf=0 svfu=1',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3285155273 t6671893446805692965 athfa3c3975 altpub cvcv=2 smf=0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v4303368379176566194 t5560511831922518437 ath259cea6f altpriv cvcv=2 smf=0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v5500155502979951206 t5629336043637742396 athe94ac249 altpriv cvcv=2 smf=0 svfu=1',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36 RuxitSynthetic/1.0 v5440167356606005062 t5596530478302100179 ath5ee645e0 altpriv cvcv=2 smf=0 svfu=1',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 RuxitSynthetic/1.0 v6388704999715157629 t7650136871829584569 athe94ac249 altpriv cvcv=2 smf=0 svfu=1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v8226397498076059084 t4900489502851206668 ath1fb31b7a altpriv cvcv=2 smf=0 svfu=1',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v3285165847 t6703941201591042144 athfa3c3975 altpub cvcv=2 smf=0',
    ]
    return random.choice(user_agent)


def crawl(produrl, collection):
    """Scraping the website, creating and connecting to the MongoDB Database to insert the scraped data"""
    # Specifying headers
    useragent = useragentselector()
    headers = {
        'authority': 'www.zaubacorp.com',
        'method': 'GET',
        'Scheme': 'https',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': '_ga=GA1.2.1027602693.1690545164; _gid=GA1.2.267303582.1690545164; __stripe_mid=2f85ccef-501d-41e1-bdb5-16437c22919677b80d; drupal.samesite=1; __stripe_sid=74f20fc1-8f90-404c-b37f-40544b19ba42e47cef; __gads=ID=f43d887916286614-22a7567000e30085:T=1690545164:RT=1690632850:S=ALNI_MYQKbZN8gsWArlxMXKSHFmpA0fplg; __gpi=UID=00000d26c03534df:T=1690545164:RT=1690632850:S=ALNI_MZjIgY2w4tyOz3WWDO3QVzBhCriyQ; _ga_VVR3BV80B8=GS1.2.1690632359.2.1.1690633123.48.0.0',
        'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        'User-Agent': useragent,
    }

    # Making a request to the URL for response HTML and parsing it
    try:
        resp = requests.get(produrl, headers=headers, timeout=30)
        resp.raise_for_status() # Raise an exception for 4xx and 5xx status codes
        prodtree = html.fromstring(resp.text)
    except requests.exceptions.RequestException as req_ex:
        print "Request Exception:", req_ex
    except HTMLParser.HTMLParseError as parse_ex:
        print "HTML Parsing Error:", parse_ex

    # Code to handle the pages crawl limit by using "Section Code" filter Category URL's to extract data
    try:
        try:
            cat_len = len(prodtree.xpath('//div[@style="width: 250px; margin: 8px; float: left;"][1]/div/ul/li/a'))
        except IndexError:
            cat_len = 0
        for c in range(cat_len):
            try:
                cat_name = prodtree.xpath('//div[@style="width: 250px; margin: 8px; float: left;"][1]/div/ul/li/a/@title')[c].strip()
            except IndexError:
                cat_name = 'n/a'

            try:
                cat_url1 = prodtree.xpath('//div[@style="width: 250px; margin: 8px; float: left;"][1]/div/ul/li/a/@href')[c].strip()
                cat_url = str(cat_url1).replace("-company.html", "")
            except IndexError:
                cat_url = 'n/a'

            try:
                cat_count = prodtree.xpath('//div[@style="width: 250px; margin: 8px; float: left;"][1]/div/ul/li/a/text()')[c].strip()
                cat_count = int(str(cat_count).split()[-1].replace("(", "").replace(")", "").replace(",", ""))
            except IndexError:
                cat_count = 0

            if cat_count > 399990:
                # Making a recursive call to the "crawl" function as limit exceeds of sub-category URL
                produrl = cat_url1
                crawl(produrl, collection)
            else:
                # Determining the number of pages to crawl
                try:
                    pagecount = int(math.ceil(cat_count / 30))
                except TypeError:
                    # Handle TypeError
                    pagecount = 0
                except ZeroDivisionError:
                    # Handle ZeroDivisionError
                    pagecount = 0

                # Scraping data page by page
                recno = 1
                for page in range(pagecount):
                    pageurl = cat_url + "/p-" + str(page+1) + "-company.html"
                    time.sleep(random.randint(2, 6))
                    try:
                        resp1 = requests.get(pageurl, headers=headers, timeout=30)
                        resp1.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
                        prodtree1 = html.fromstring(resp1.text)
                    except requests.exceptions.RequestException as req_ex:
                        print "Request Exception:", req_ex
                    except HTMLParser.HTMLParseError as parse_ex:
                        print "Page HTML Parsing Error:", parse_ex

                    # Looping through all the companies in the page and extracting required data

                    comp = 1
                    while prodtree1.xpath('//tr['+str(comp)+']/td') != []:
                        try:
                            cin = prodtree1.xpath('//tr['+str(comp)+']/td[1]/text()')[0].strip()
                        except IndexError:
                            cin = 'n/a'

                        try:
                            company = prodtree1.xpath('//tr['+str(comp)+']/td[2]/a/text()')[0].strip()
                        except IndexError:
                            company = 'n/a'

                        try:
                            company_url = prodtree1.xpath('//tr['+str(comp)+']/td[2]/a/@href')[0].strip()
                        except IndexError:
                            company_url = 'n/a'

                        try:
                            roc = prodtree1.xpath('//tr['+str(comp)+']/td[3]/text()')[0].strip()
                        except IndexError:
                            roc = 'n/a'

                        try:
                            status = prodtree1.xpath('//tr['+str(comp)+']/td[4]/text()')[0].strip()
                        except IndexError:
                            status = 'n/a'

                        record = {"Record_No": recno, "CIN": cin, "Company": company, "Company_URL": company_url,
                                  "RoC": roc, "Status": status, "Category_Name": cat_name, "Crawl_URL": pageurl,
                                  "Category_Count": cat_count}

                        print recno
                        print company
                        print status
                        print pageurl
                        print "CATEGORY_COUNT:", cat_count
                        print "PAGE_COUNT:", pagecount

                        comp += 1
                        recno += 1

                        # Insert the scraped data into MongoDB collection
                        collection.insert_one(record)

        return "Crawl Completed"
    except Exception as exp:
        print "Execution Failed:", exp


# Connect to MongoDB and create a database and collection

# CONNECTION_URL = "mongodb+srv://dheerajnair98:LDamsPf1TdGbcFgA@cluster0.wlmugio.mongodb.net/?retryWrites=true&w=majority"

CONNECTION_URL = "mongodb+srv://<USERNAME>:<PASSWORD>@<CLUSTER_URL>/test?retryWrites=true&w=majority"
CLIENT = pymongo.MongoClient(CONNECTION_URL)
DATABASE = CLIENT['ZaubaCorp']
COLLECTION = DATABASE['Companies']

# Close the MongoDB connection
CLIENT.close()

# Script Caller

PRODURL = "https://www.zaubacorp.com/company-list-company.html"
PDP = crawl(PRODURL, COLLECTION) # Scrape Execution Function Calling
