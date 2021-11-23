from element import EspolEducationElement
from locators import EspolEducationLocators, CareerPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import openpyxl
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver, list_href):
        self.driver = driver
        self.list_href = list_href


class EspolEducationPage(BasePage):

    def get_faculties(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(EspolEducationLocators.FACULTY_LIST))

    def get_classes(self, codigo):
        return self.driver.find_elements(By.XPATH, '//div[@id="'+codigo+'"]//div[@class="field-content"]//ul//li//a')

    def create_excel_file(self):
        wb = openpyxl.Workbook()
        hoja = wb.create_sheet("Hoja")
        hoja.append(('Carrera', 'Facultad', 'Link'))

        facultades = self.get_faculties()
        href = []

        #Leer nombres de las facultades
        i = 0
        c = 0
        for facultad in facultades:
            codigo = facultad.get_attribute("href").split("#")[-1]

            i = i + 1
            if (i < 5):
                self.driver.execute_script("arguments[0].scrollIntoView(true);", facultad)
                self.driver.execute_script("arguments[0].click();", facultad)
                ActionChains(self.driver).click_and_hold(facultad).perform()
            else:
                self.driver.execute_script("window.scrollTo(0, 0);")
                self.driver.execute_script("arguments[0].click();", facultad)
                
            #Leer nombres de las materias
            if (facultad.get_attribute("aria-expanded")):
                todas_las_materias = self.get_classes(codigo)
                for materia in todas_las_materias:
                    href.append(materia.get_attribute("href"))

                    c = c + 1
                    hoja.cell(row=c, column=1).value = materia.text
                    hoja.cell(row=c, column=2).value= facultad.text
                    hoja.cell(row=c, column=3).value= materia.get_attribute("href")
                    print(materia.text)
                    print(facultad.text)
                    print(materia.get_attribute("href"))
    
        wb.save('educacion_espol.xlsx')
        self.list_href = href
    
    def show_abet_list(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

        abet_list = []

        principal_window = self.driver.current_window_handle

        for href in self.list_href:
            print(href)
            element = WebDriverWait(self.driver, 25).until(EC.presence_of_element_located((By.LINK_TEXT, href)))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            self.driver.execute_script("arguments[0].click();", element)

            try:
                abet = CareerEducationPage.is_abet(self)
                if 'abet' in abet.text:
                    abet_list.append(abet.text)
            finally:
                print("no es abet")
            
            self.driver.switch_to.window(principal_window)
        
        print(abet_list)
                

class CareerEducationPage(BasePage):
    """Search results page action methods come here"""

    def is_abet(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return WebDriverWait(self.driver, 100).until(EC.presence_of_element_located(CareerPageLocators.ABET_HREF))