import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#from webdriver_manager.firefox import GeckoDriverManager

def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.driver = webdriver.Chrome(executable_path="C:\\Users\\User\\Downloads\\chromedriver.exe", chrome_options=options)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.espol.edu.ec/es/educacion")
        facultades = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="panel-heading"]//h4[@class="panel-title"]//a')))
        
        i = 0
        for facultad in facultades:
            i = i + 1
            print(facultad.get_attribute("href").split("#")[-1])
            print(facultad.text)

            if (i < 5):
                driver.execute_script("arguments[0].scrollIntoView(true);", facultad)
                driver.execute_script("arguments[0].click();", facultad)
                ActionChains(driver).click_and_hold(facultad).perform()
            else:
                driver.execute_script("arguments[0].setAttribute('class','accordion-toggle')", facultad)
                driver.execute_script("arguments[0].setAttribute('aria-expanded','true')", facultad)
                
            #Leer nombres de las materias
            if (facultad.get_attribute("aria-expanded")):
                todas_las_materias = driver.find_elements(By.XPATH, '//div[@id="'+facultad.get_attribute("href").split("#")[-1]+'"]//div[@class="field-content"]//ul//li//a')
                for materia in todas_las_materias:
                    driver.execute_script("arguments[0].setAttribute('class','panel-collapse collapse in')", materia)
                    driver.execute_script("arguments[0].setAttribute('aria-expanded','true')", materia)
                    driver.execute_script("arguments[0].setAttribute('style','')", materia)
                    print("Materia")
                    print(materia.get_attribute("href"))
                    print(materia.text)
                

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()