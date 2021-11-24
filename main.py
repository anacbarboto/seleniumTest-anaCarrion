import unittest
from selenium import webdriver
import page


class ESPOLSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path="chromeDriver\chromedriver.exe", chrome_options=options)
        self.driver.maximize_window()
        self.driver.get("https://www.espol.edu.ec/es/educacion")

    def test_search_in_espol(self):
        #Load the main page. In this case the home page of Python.org.
        main_page = page.EspolEducationPage(self.driver, [], [])

        #Create a excel file
        main_page.create_excel_file()
        
        #Create and print a list of carees that has abet certification
        main_page.show_abet_list()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(warnings='ignore')





    