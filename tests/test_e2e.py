from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import pytest

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.HomePage import HomePage
from utility.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        homePage.shopItems().click()
        #self.driver.find_element(By.CSS_SELECTOR, value=" a[href*='shop']").click()
        checkoutPage = CheckoutPage(self.driver)
        #checkoutPage = homePage.shopItems()
        cards = checkoutPage.getCardTitle()
        i = -1
        for card in cards:
            i = i+1
            cardText = card.text
            print(cardText)
            if cardText == "Blackberry":
                checkoutPage.getCardFooter()[i].click()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkoutPage.CheckoutItems().click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text
        assert "Success! Thank you!" in successText





