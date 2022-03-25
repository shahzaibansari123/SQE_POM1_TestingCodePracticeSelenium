from selenium.webdriver.common.by import By

class alerts:
    def __init__(self,driver):
        self.driver = driver
        self.alert1 = "alertButton"


    def alert_button(self):
        self.driver.find_element(By.ID, self.alert1).click()

