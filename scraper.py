from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, web, topic):
        self.topic = topic
        self.web_content = web
        self.soup = BeautifulSoup(self.web_content, "html.parser")

    def get_jobs(self):
        data = self.soup
        jobs_section = data.find(name='section', class_='card-list-container')
        if jobs_section:
            # find number of pages
            page_numbers = data.find_all(name='div', class_='sr-only')
            print(int(page_numbers[-2].text[24::].lstrip()))
            return jobs_section
        else:
            print(f"Sorry not jobs found for: '{self.topic}'")
            exit(0)
