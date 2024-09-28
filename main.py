from web import Web
from scraper import Scraper
from data import Data

topic = input("Please type your work topic E.g: python. ").strip()

# get web content
web = Web(topic=topic)
web_content = web.get_webpage()
# scrape data
scraper = Scraper(web=web_content, topic=topic)
scraper.get_info()
# create data of content
data = Data(scraper.job_title, scraper.job_description, scraper.job_payment, scraper.job_link, topic)
# create csv of data
data.crate_cvs()

