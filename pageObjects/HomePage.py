from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage
from utility.BaseClass import BaseClass


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, " a[href*='shop']")
    name = (By.XPATH, "//input[@name='name' and @minlength='2']")
    email = (By.XPATH, "//input[@name='email']")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@value='Submit']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)
        #checkoutPage = CheckoutPage(self.driver)
        #return checkoutPage

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def pressButton(self):
        return self.driver.find_element(*HomePage.submit)

