from selenium.webdriver.support.ui import WebDriverWait


class EspolEducationElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""


    def __get__(self, obj, owner):
        """Gets the text of the specified object"""
