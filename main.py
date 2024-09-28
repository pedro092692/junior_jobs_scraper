from web import Web
from scraper import Scraper

topic = 'python'

web = Web(topic='python')
web_content = web.get_webpage()


scraper = Scraper(web=web_content, topic=topic)
scraper.get_info()
