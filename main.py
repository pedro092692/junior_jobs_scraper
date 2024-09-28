from web import Web
from scraper import Scraper

topic = 'python'

web = Web()
web_content = web.get_webpage(topic=topic)


scraper = Scraper(web=web_content, topic=topic)
print(scraper.get_info())
