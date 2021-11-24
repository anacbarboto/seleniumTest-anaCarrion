from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from locators import EspolEducationLocators, CareerEducationLocators


class EspolEducationElement(object):
    def get_faculties(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(EspolEducationLocators.FACULTY_LIST))

    def get_classes(self, code):
        return self.driver.find_elements(By.XPATH, '//div[@id="'+code+'"]//div[@class="field-content"]//ul//li//a')

class CareerEducationElement(object):
    def is_abet(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(CareerEducationLocators.ABET_HREF))
    
    def is_oceanography_abet(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(CareerEducationLocators.ABET_OCEANOGRAPHY))
    
    def is_food_abet(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(CareerEducationLocators.ABET_FOOD))