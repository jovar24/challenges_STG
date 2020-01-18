import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class challenge2(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def test_challenge2(self):
        driver = self.driver
        driver.get("https://www.copart.com/")
        pagetitle = driver.title
        self.assertEqual("Auto Auction - Copart USA - Salvage Cars for Sale in Online Car Auctions", pagetitle, "title is not the same")
        elem = driver.find_element_by_id("input-search")
        elem.send_keys("exotic")
        elem.send_keys(Keys.RETURN)
        findporsche = self.driver.find_elements(By.XPATH, "//*[@id='serverSideDataTable']/tbody")
        print(findporsche.__getattribute__("data-uname"))


    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
            unittest.main()
