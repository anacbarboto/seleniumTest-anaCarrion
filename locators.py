from selenium.webdriver.common.by import By

class EspolEducationLocators(object):
    """A class for main page locators. All main page locators should come here"""

    FACULTY_LIST = (By.XPATH, '//div[@class="panel-heading"]//h4[@class="panel-title"]//a')

class CareerPageLocators(object):
    """A class for search results locators. All search results locators should
    come here"""

    ABET_HREF = (By.XPATH, '//a[@href="http://www.abet.org"]')