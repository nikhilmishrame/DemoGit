import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from TestData.HomePageTestData import HomePageTestData
from pageObjects.HomePage import HomePage
from utility.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, getData):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        log.info(self.driver.title)
        log.info("Entering First Name :"+getData["FirstName"])
        homepage.getName().send_keys(getData["FirstName"])
        log.info("Entering Email :"+getData["Email"])
        homepage.getEmail().send_keys(getData["Email"])
        log.info("Entering Gender :"+getData["Gender"])
        self.selectOptionByText(homepage.getGender(), getData["Gender"])
        homepage.pressButton()
        self.driver.refresh()
        # self.driver.find_element(By.CSS_SELECTOR, " a[href*='shop']").click()
        # products = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        #
        # for product in products:
        #     productName = product.find_element(By.XPATH, "div/h4/a").text
        #     if productName == "Blackberry":
        #         product.find_element(By.XPATH, "div/button").click()
        #
        # self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        # self.driver.find_element(By.ID, "country").send_keys("ind")
        # wait = WebDriverWait(self.driver, 10)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        # self.driver.find_element(By.LINK_TEXT, "India").click()
        # self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        # successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        #assert "Success! Thank you!" in self.driver.title




    @pytest.fixture(params=HomePageTestData.homePageTestData)
    def getData(self, request):
        return request.param
