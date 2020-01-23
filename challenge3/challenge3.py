import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        self.driver.get("https://www.copart.com")
        listofelements = self.driver.find_elements(By.XPATH, '//*[@ng-if="popularSearches"]//a')
        listofelements2 = self.driver.find_elements(By.XPATH, '//*[@ng-if="popularSearches"]/../div[3]//a')
        count = 0
        while count < len(listofelements):
            print(listofelements[count].text+":"+listofelements2[count].get_attribute("href"))
            count += 1


if __name__ == '__main__':
    unittest.main()
