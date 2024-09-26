from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Browser:

    def __init__(self):

        self.url = 'https://www.upwork.com/nx/search/jobs/?contractor_tier=1&q=python&sort=recency'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.url)

    def seek_job(self):
        search_input = self.driver.find_element(By.ID, value='searchBar-jobTitle')
        self.driver.execute_script("arguments[0].setAttribute('value', 'python')", search_input)


browser = Browser()
browser.seek_job()