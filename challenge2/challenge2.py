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
        assert "Copart" in driver.title
        elem = driver.find_element_by_id("input-search")
        elem.send_keys("exotics")
        elem.send_keys(Keys.RETURN)
        findPorsche = driver.find_element(By.XPATH, '//table[@id="serverSideDataTable"]/tbody/tr/td[5]/span')
        print(findPorsche.get_attribute("span"))



    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
            unittest.main()
