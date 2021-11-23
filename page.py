from element import EspolEducationElement
from locators import EspolEducationLocators, CareerPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import openpyxl


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver


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
                self.driver.execute_script("arguments[0].setAttribute('class','accordion-toggle')", facultad)
                self.driver.execute_script("arguments[0].setAttribute('aria-expanded','true')", facultad)
                
            #Leer nombres de las materias
            if (facultad.get_attribute("aria-expanded")):
                todas_las_materias = self.get_classes(codigo)
                for materia in todas_las_materias:
                    self.driver.execute_script("arguments[0].setAttribute('class','panel-collapse collapse in')", materia)
                    self.driver.execute_script("arguments[0].setAttribute('aria-expanded','true')", materia)
                    self.driver.execute_script("arguments[0].setAttribute('style','')", materia)
                    
                    c = c + 1
                    hoja.cell(row=c, column=1).value = materia.text
                    hoja.cell(row=c, column=2).value= facultad.text
                    hoja.cell(row=c, column=3).value= materia.get_attribute("href")
                    print(materia.text)
                    print(facultad.text)
                    print(materia.get_attribute("href"))
    
        wb.save('educacion_espol.xlsx')
    
    def show_abet_list(self):
        print("show list")


class CareerEducationPage(BasePage):
    """Search results page action methods come here"""

    def is_abet(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(CareerPageLocators.ABET_HREF))