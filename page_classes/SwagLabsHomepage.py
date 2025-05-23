from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver # For autocomplete


class SwagLabsHomepage:
    #Step 1: Define web elements as class variables
    textBackpackProductXpath = "//div[text()='Sauce Labs Backpack']"
    allProductSizeXpath = "//div[@class='inventory_item_name ']"
    textBackpackProductPriceXpath = "(//div[@class='inventory_item_price'])[1]"
    textAllProductTotalPriceXpath = "//div[@class='inventory_item_price']"

    #Step 2: Declare and initialize the WebDriver object
    def __init__(self,driver: WebDriver):
        self.driver = driver

    #Step 3: Perform Actions
    def getBackpackProductName(self):
        productName = self.driver.find_element(By.XPATH, self.textBackpackProductXpath).text
        return productName

    def getAllProductSize(self):
        allProductSize = self.driver.find_elements(By.XPATH, self.allProductSizeXpath)
        size = len(allProductSize)
        return size

    def getBackpackProductPrice(self):
        backpackProductPrice = self.driver.find_element(By.XPATH, self.textBackpackProductPriceXpath).text
        productPrice = backpackProductPrice[1:]
        return productPrice

    def getAllProductTotalPrice(self):
        allProductPrice = self.driver.find_elements(By.XPATH, self.textAllProductTotalPriceXpath)
        totalPrice = 0
        for i in allProductPrice:
            s1 = i.text  # $32.5  -> convert WebElement to Text
            s1 = s1[1:]  # 32.5 -> String   -> remove char from string
            s1 = float(s1)  # 32.5 -> float    -> covert String to float
            totalPrice = totalPrice + s1
        return totalPrice