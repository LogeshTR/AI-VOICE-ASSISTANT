from selenium import webdriver

class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='D:\\Logesh T R\\AI-Voice-Assistant-main\\chromedriver.exe')

    def getinfo(self,query):
        self.query = query
        self.driver.get(url="https://wikipedia.org")
        xpath = '//*[@id="searchInput"]'
        search=self.driver.find_element_by_xpath(xpath)
        search.click()
        search.send_keys(query)
        xpath1 = '//*[@id="search-form"]/fieldset/button'
        enter=self.driver.find_element_by_xpath(xpath1)
        enter.click()

