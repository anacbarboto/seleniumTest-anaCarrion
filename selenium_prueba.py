import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#from webdriver_manager.firefox import GeckoDriverManager

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C:\\Users\\User\\Downloads\\chromedriver.exe")

    def test_search_in_python_org(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.espol.edu.ec/es/educacion")
        facultades_izquierda = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//section[@id="block-views-facultades-block"]//h4[@class="panel-title"]//a')))
        
        i = 0
        for facultad in facultades_izquierda:
            i = i + 1
            print(facultad.get_attribute("href").split("#")[-1])
            print(facultad.text)
            
            #facultad.location_once_scrolled_into_view
            if (i > 2):
                driver.execute_script("arguments[0].scrollIntoView();", facultad)
            
            driver.execute_script("arguments[0].click();", facultad)
            ActionChains(driver).click_and_hold(facultad).perform()
            #ActionChains(driver).release(facultad).perform()
            
            #driver.execute_script("arguments[0].setAttribute('aria-expanded','true')", facultad)
            if (facultad.get_attribute("aria-expanded")):
                todas_las_materias = driver.find_elements(By.XPATH, '//div[@id="'+facultad.get_attribute("href").split("#")[-1]+'"]//div[@class="field-content"]//ul//li//a')
                for materia in todas_las_materias:
                    print(materia.get_attribute("href"))
                    print(materia.text)
            print("-------------------------------------------------")
        
        facultades_derecha = driver.find_elements(By.XPATH, '//section[@id="block-views-facultades-block-1"]//h4[@class="panel-title"]//a')
        j = 0
        for f in facultades_derecha:
            j = j + 1
            print(f.get_attribute("href").split("#")[-1])
            print(f.text)

            ActionChains(driver).move_to_element(f).click().perform()
            
            #driver.execute_script("arguments[0].setAttribute('aria-expanded','true')", facultad)
            if (f.get_attribute("aria-expanded")):
                todas_las_materias = driver.find_elements(By.XPATH, '//div[@id="'+f.get_attribute("href").split("#")[-1]+'"]//div[@class="field-content"]//ul//li//a')
                for materia in todas_las_materias:
                    print(materia.get_attribute("href"))
                    print(materia.text)
            print("-------------------------------------------------")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()