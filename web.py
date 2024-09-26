import cloudscraper
import requests

class Web:

    def __init__(self):
        self.scraper = cloudscraper.create_scraper(
            browser={
                'browser': 'firefox',
                'platform': 'windows',
                'mobile': False
            },
        )

    def get_webpage(self, topic: str) -> str:
        url = f'https://www.upwork.com/nx/search/jobs/?contractor_tier=1&q={topic}&sort=recency'
        try:
            response = self.scraper.get(url)
            response.raise_for_status()
            web_content = response.text
        except requests.exceptions.ConnectionError as e:
            print('Error connection to web page')
        else:
            return web_content
