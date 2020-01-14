import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class challenge2(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def test_challenge2(self):
        driver = self.driver
        driver.get("https://www.copart.com/")
        elem = driver.find_element_by_id("input-search")
        elem.send_keys("exotic")
        elem.send_keys(Keys.RETURN)
        tablesearch = self.driver.find_element_by_xpath("//ul[@class='list-unstyled scroll-put']").text
        self.assertEqual(tablesearch, "Porsche", "porsche was not in list")

    def tearDown(self):
        self.driver.close()

    if __name__ == '__main__':
            unittest.main()
