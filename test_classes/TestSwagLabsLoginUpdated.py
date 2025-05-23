import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page_classes.SwagLabsHomepage import SwagLabsHomepage
from page_classes.SwagLabsLoginPage import SwagLabsLoginPage
from utility_files.custom_logger import LogGen
from utility_files.read_excel import ReadTestData
from utility_files.read_properties import ReadConfig


class TestSwagLabsLogin:
    logger = LogGen.log_gen()

    def loginToApp(self,driver):
        login = SwagLabsLoginPage(driver)
        login.enter_username(ReadConfig.getUsername())
        login.enter_password(ReadConfig.getPassword())
        login.click_login_button()


    @pytest.mark.sanity
    def test_TC1_login_with_valid_credentials(self,open_browser):
        self.logger.info("----------Test case 1 execution started----------")
        self.logger.info("----------test_login_with_valid_credentials----------")
        driver = open_browser
        self.loginToApp(driver)
        actTitle = driver.title
        expTitle = ReadTestData.getTestData(1,1)
        if actTitle==expTitle:
            assert True
            self.logger.info("----------Passed: The actual title and expected title match----------")
        else:
            driver.save_screenshot("screenshots/test_TC1_login_with_valid_credentials.png")
            self.logger.info("----------Failed: The actual title and expected title mismatch----------")
            assert False
        time.sleep(5)
        driver.quit()

    @pytest.mark.smoke
    def test_TC2_login_with_invalid_credentials(self,open_browser):
        self.logger.info("----------Test case 2 execution started----------")
        self.logger.info("----------test_login_with_invalid_credentials----------")
        username = "test_user"
        password = "test_password"

        driver = open_browser

        login = SwagLabsLoginPage(driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login_button()

        self.logger.info("----------Passed: The system should reject the login attempt and display an appropriate error message.----------")
        driver.save_screenshot(".\\screenshots\\test_TC2_login_with_invalid_credentials.png")

        time.sleep(5)
        driver.quit()

    @pytest.mark.regression
    def test_TC3_verify_product_name(self,open_browser):
        self.logger.info("----------Test case 3 execution started----------")
        self.logger.info("----------verify_product_name----------")
        driver = open_browser
        self.loginToApp(driver)
        home = SwagLabsHomepage(driver)
        actProductName = home.getBackpackProductName()
        expProductName = ReadTestData.getTestData(3, 1)
        if actProductName == expProductName:
            assert True
            self.logger.info("----------Passed: The actual product name and expected product name match----------")
        else:
            driver.save_screenshot("screenshots/test_TC3_verify_product_name.png")
            self.logger.info("----------Failed: The actual product name and expected product name mismatch----------")
            assert False
        time.sleep(5)
        driver.quit()

    @pytest.mark.regression
    def test_TC4_verify_product_size(self,open_browser):
        self.logger.info("----------Test case 4 execution started----------")
        self.logger.info("----------verify_product_size----------")
        driver = open_browser
        self.loginToApp(driver)
        home = SwagLabsHomepage(driver)
        actProductSize = home.getAllProductSize()
        expProductSize = ReadTestData.getTestDataInt(4,1)
        if actProductSize == expProductSize:
            assert True
            self.logger.info("----------Passed: The actual size and expected product size match----------")
        else:
            driver.save_screenshot("screenshots/test_TC4_verify_product_size.png")
            self.logger.info("----------Failed: The actual product size and expected product size mismatch----------")
            assert False
        time.sleep(5)
        driver.quit()

    @pytest.mark.regression
    def test_TC5_verify_product_price(self, open_browser):
        self.logger.info("----------Test case 5 execution started----------")
        self.logger.info("----------verify_product_price----------")
        driver = open_browser
        self.loginToApp(driver)
        home = SwagLabsHomepage(driver)
        actProductPrice = float(home.getBackpackProductPrice())
        expProductPrice = float(ReadTestData.getTestData(5, 1))
        if actProductPrice == expProductPrice:
            assert True
            self.logger.info("----------Passed: The actual price and expected product price match----------")
        else:
            driver.save_screenshot("screenshots/test_TC5_verify_product_price.png")
            self.logger.info("----------Failed: The actual product price and expected product price mismatch----------")
            assert False
        time.sleep(5)
        driver.quit()

    @pytest.mark.regression
    def test_TC6_verify_all_product_price(self, open_browser):
        self.logger.info("----------Test case 6 execution started----------")
        self.logger.info("----------verify_all_product_price----------")
        driver = open_browser
        self.loginToApp(driver)
        home = SwagLabsHomepage(driver)
        actTotalPrice = home.getAllProductTotalPrice()
        expTotalPrice = float(ReadTestData.getTestData(6,1))
        if actTotalPrice == expTotalPrice:
            assert True
            self.logger.info("----------Passed: The actual total price and expected total product price match----------")
        else:
            driver.save_screenshot("screenshots/C6_verify_all_product_price.png")
            self.logger.info("----------Failed: The actual total product price and expected total product price mismatch----------")
            assert False
        time.sleep(5)
        driver.quit()