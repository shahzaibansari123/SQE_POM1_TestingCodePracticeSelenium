from selenium.webdriver.common.by import By


class practiceform:
    def __init__(self,driver):
        self.driver = driver
        self.firstname = "firstName"
        self.lastname = "lastName"

    def enter_firstname(self, fname):
        self.driver.find_element(By.ID, self.firstname).send_keys(fname)

    def enter_lastname(self, lname):
        self.driver.find_element(By.ID, self.lastname).send_keys(lname)


