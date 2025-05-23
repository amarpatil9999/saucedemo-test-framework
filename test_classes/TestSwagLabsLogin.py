import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from page_classes.SwagLabsLoginPage import SwagLabsLoginPage
from utility_files.custom_logger import LogGen
from utility_files.read_excel import ReadTestData
from utility_files.read_properties import ReadConfig


class TestSwagLabsLogin:    # Class names always begin with the test word
    # Rewritten Version (Using configparser -> Fetch the methods):
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    url = ReadConfig.getURL()
    logger = LogGen.log_gen()

    def test_login_with_valid_credentials(self,open_browser):    #Method names always begin with the test word
        self.logger.info("----------1st Test case execution started----------")
        self.logger.info("----------test_login_with_valid_credentials----------")

        # Commenting out the username, password, and URL fields to reduce code, and using configparser to retrieve these values.
        # Hardcoded Version:
        # username = "standard_user"
        # password = "secret_sauce"
        # url = "https://www.saucedemo.com/"

        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")

        # driver = webdriver.Chrome(options=chrome_options)
        # driver.get("https://www.saucedemo.com/")
        driver = open_browser   # use fixture here
        # driver.get(url)   # Commenting out since we are using configparser.
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(5)

        login = SwagLabsLoginPage(driver)
        # login.enter_username(username)    # Commenting out since we are using configparser.
        # login.enter_password(password)    # Commenting out since we are using configparser.
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login_button()

        actTitle = driver.title
        # expTitle = "Swag Labs"
        expTitle = ReadTestData.getTestData(1,1)
        if actTitle==expTitle:
            assert True
            self.logger.info("----------Passed: The actual title and expected title match----------")
        else:
            driver.save_screenshot("screenshots/test_login_with_valid_credentials_01.png")
            # driver.save_screenshot(".\\screenshots\\test_login_with_valid_credentials_02.png")
            self.logger.info("----------Failed: The actual title and expected title mismatch----------")
            assert False
        time.sleep(5)
        driver.quit()
"""
    def test_login_with_invalid_credentials(self,open_browser):
        self.logger.info("----------2nd Test case execution started----------")
        self.logger.info("----------test_login_with_invalid_credentials----------")
        username = "test_user"
        password = "test_password"
        # url = "https://www.saucedemo.com/"

        # driver = webdriver.Chrome()
        driver = open_browser
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(5)

        login = SwagLabsLoginPage(driver)
        login.enter_username(username)
        login.enter_password(password)
        login.click_login_button()

        # driver.save_screenshot("screenshots/test_login_with_invalid_credentials_01.png")
        driver.save_screenshot(".\\screenshots\\test_login_with_invalid_credentials_02.png")

        time.sleep(5)
        driver.quit()
"""
