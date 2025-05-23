from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver # For autocomplete


class SwagLabsLoginPage:
    #Step 1: Define web elements as class variables
    inpUsernameXPath = "//input[@id='user-name']"
    inPasswordXPath = "//input[@id='password']"
    btnLoginXPath = "//input[@id='login-button']"

    #Step 2: Declare and initialize the WebDriver object
    def __init__(self,driver: WebDriver):
        self.driver = driver

    #Step 3: Perform Actions
    #First Snippet (Hardcoded Input Version)
    # def enter_username(self):
    #     self.driver.find_element(By.XPATH,self.inpUsernameXPath).send_keys("standard_user")
    #
    # def enter_password(self):
    #     self.driver.find_element(By.XPATH,self.inPasswordXPath).send_keys("secret_sauce")

    #Second Snippet (Dynamic Input via Parameters)
    def enter_username(self, usernameValue):
        self.driver.find_element(By.XPATH, self.inpUsernameXPath).send_keys(usernameValue)

    def enter_password(self, passwordValue):
        self.driver.find_element(By.XPATH, self.inPasswordXPath).send_keys(passwordValue)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.btnLoginXPath).click()