from element import EspolEducationElement
from locators import EspolEducationLocators, CareerPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import openpyxl
import time
import warnings

warnings.simplefilter("ignore", ResourceWarning)


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver, list_href, careers_name):
        self.driver = driver
        self.list_href = list_href
        self.careers_name = careers_name


class EspolEducationPage(BasePage):
    def get_faculties(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(EspolEducationLocators.FACULTY_LIST))

    def get_classes(self, codigo):
        return self.driver.find_elements(By.XPATH, '//div[@id="'+codigo+'"]//div[@class="field-content"]//ul//li//a')

    def create_excel_file(self):
        print("Creating an excel file.")
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = 'Carreras de ESPOL'
        ws.append(('Carrera', 'Facultad', 'Link'))

        faculties = self.get_faculties()
        list_href = []
        list_careers_name = []

        i = 0
        z = 0
        for f in faculties:
            code_id = f.get_attribute("href").split("#")[-1]
            print(f.text)
            i = i + 1
            if (i < 5):
                self.driver.execute_script("arguments[0].scrollIntoView(true);", f)
                self.driver.execute_script("arguments[0].click();", f)
                ActionChains(self.driver).click_and_hold(f).perform()
            else:
                self.driver.execute_script("window.scrollTo(0, 0);")
                self.driver.execute_script("arguments[0].click();", f)
                
            if (f.get_attribute("aria-expanded")):
                careers = self.get_classes(code_id)
                for c in careers:
                    list_href.append(c.get_attribute("href"))
                    list_careers_name.append(c.text)

                    z = z + 1
                    ws.cell(row=z, column=1).value = c.text
                    ws.cell(row=z, column=2).value= f.text
                    ws.cell(row=z, column=3).value= c.get_attribute("href")
                    print(c.text)
                    print(c.get_attribute("href"))
    
        wb.save('educacion_espol.xlsx')
        wb.close()
        self.list_href = list_href
        self.careers_name = list_careers_name
        print("educacion_espol.xlsx was saved.")
    
    def show_abet_list(self):
        print("Searching careers which have abet certification.")
        abet_list = []
        list_href = self.list_href
        j = 0
        for href in list_href:
            self.driver.get(href)
            try:
                if (j != 25):
                    if (j == 31):
                        abet = CareerEducationPage.is_oceanography_abet(self)
                    else:
                        abet = CareerEducationPage.is_abet(self)
                    
                    if 'abet' in abet.text:
                        abet_list.append(self.careers_name[j])
                else:
                    abet = CareerEducationPage.is_food_abet(self)
                    abet_list.append(self.careers_name[j])
            except TimeoutException as ex:
                print("TimeoutException occurs, one career doesn't have abet certification.")
            j = j + 1
        print("Careers which have abet certification are:")
        for element in abet_list:
            print(element)

class CareerEducationPage(BasePage):
    def is_abet(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(CareerPageLocators.ABET_HREF))
    
    def is_oceanography_abet(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(CareerPageLocators.ABET_OCEANOGRAPHY))
    
    def is_food_abet(self):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(CareerPageLocators.ABET_FOOD))