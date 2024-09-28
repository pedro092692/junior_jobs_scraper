from attr import attributes
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, web, topic):
        self.topic = topic
        self.web_content = web
        self.soup = BeautifulSoup(self.web_content, "html.parser")

        self.job_title = []
        self.job_description = []
        self.job_payment = []
        self.job_link = []

    def get_info(self):
        data = self.soup
        jobs_section = data.find(name='section', class_='card-list-container')
        if jobs_section:
            # find number of pages
            number_of_pages = int(data.find_all(name='div', class_='sr-only')[-2].text[24::].lstrip())

            # get job info from jobs section
            jobs_articles = jobs_section.find_all(name='article')

            # get job titles
            self.get_job_titles(jobs_list=jobs_articles)

            # get job description
            self.get_job_description(jobs_list=jobs_articles)

            # get job python
            self.get_job_payment(job_list=jobs_articles)

            #get job link
            self.get_job_link(job_list=jobs_articles)


        else:
            print(f"Sorry not jobs found for: '{self.topic}'")
            exit(0)


    def get_job_titles(self, jobs_list: list):
        for artitle in jobs_list:
            job_title = artitle.find(name='h2', class_='job-tile-title')
            self.job_title.append(job_title.text)


    def get_job_description(self, jobs_list: list):
        for article in jobs_list:
            job_description = article.select_one('.is-clamped p')
            self.job_description.append(job_description.text)


    def get_job_payment(self, job_list: list):
        for article in job_list:
            job_info = article.find(name='ul', class_='job-tile-info-list')
            job_payment = job_info.find(name='li', attrs={"data-test": "is-fixed-price"})
            if not job_payment:
                job_payment = job_info.find(name='li', attrs={"data-test": "job-type-label"})
            self.job_payment.append(job_payment)


    def get_job_link(self, job_list: list):
        for article in job_list:
            link = article.find(name='a', attrs={"data-test": "job-tile-title-link"})
            job_url = f'https://www.upwork.com/freelance-jobs/apply/{link["href"].split("/")[2]}'
            self.job_link.append(job_url)
