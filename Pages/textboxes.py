from selenium.webdriver.common.by import By


class textboxes:
    def __init__(self,driver):
        self.driver = driver
        self.fullname_ID = "userName"
        self.email = "userEmail"
        self.c_address = "currentAddress"
        self.p_address = "permanentAddress"
        self.submit_btn = "submit"
        # self.goToForm= " // *[ @ id = "app"] / div / div / div[2] / div / div[1]"
        # self.openForm="/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/ul/li"


    def enter_fullname(self,name):
        self.driver.find_element(By.ID,self.fullname_ID).send_keys(name)

    def enter_email(self,mail):
        self.driver.find_element(By.ID, self.email).send_keys(mail)

    def enter_address(self,caddress):
        self.driver.find_element(By.ID, self.c_address).send_keys(caddress)

    def enter_perm_address(self,paddress):
        self.driver.find_element(By.ID, self.p_address).send_keys(paddress)

    def click_submit(self):
        self.driver.find_element(By.ID,self.submit_btn).click()

    # def go_to_form(self):
    #     self.driver.find_element(By.XPATH,self.goToForm).click()
    #
    # def open_form(self):
    #     self.driver.find_element(By.XPATH, self.openForm).click()