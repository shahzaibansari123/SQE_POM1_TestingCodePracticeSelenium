import time
import unittest
from Pages.textboxes import textboxes
from Pages.Practiceform import practiceform
from Pages.alerts import alerts
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
class DemoQAtests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver  = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.get("https://demoqa.com/")
        cls.driver.maximize_window()

    def test_filltextboxes(self):
        driver = self.driver
        driver.get("https://demoqa.com/text-box")
        text = textboxes(driver)
        text.enter_fullname("Shahzaib Ansari")
        text.enter_email("ansarishahzaib567@gmail.com")
        text.enter_address("Liaquatabad Karachi")
        text.enter_perm_address("Karachi")
        time.sleep(5)
        text.click_submit()
        time.sleep(3)

    def test_practiceform(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.get("https://demoqa.com/automation-practice-form")

        pForm=practiceform(driver)
        pForm.enter_firstname("Shahzaib")
        pForm.enter_lastname("Ansari")

    def test_alert(self):
        driver = self.driver
        driver.implicitly_wait(3)
        driver.get("https://demoqa.com/alerts")

        pAlert = alerts(driver)
        pAlert.alert_button()
        time.sleep(3)

    @classmethod
    def tearDownClass1(cls):
        cls.driver.close()
        cls.driver.quit()

# class practiceForm(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver  = webdriver.Chrome(ChromeDriverManager().install())
#         cls.driver.get("https://demoqa.com/automation-practice-form")
#         cls.driver.maximize_window()
#
#     def test_practiceform(self):
#         driver = self.driver
#         pForm=practiceform(driver)
#         pForm.enter_firstname("Shahzaib")
#         pForm.enter_lastname("Ansari")
#
#     @classmethod
#     def tearDownClass1(cls):
#         cls.driver.close()
#         cls.driver.quit()
#
#
# class prctalerts(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome(ChromeDriverManager().install())
#         cls.driver.get("https://demoqa.com/alerts")
#         cls.driver.maximize_window()
#
#     def test_alert(self):
#         driver = self.driver
#         pAlert = alerts(driver)
#         pAlert.alert_button()
#         time.sleep(3)
#
#     @classmethod
#     def tearDownClass1(cls):
#         cls.driver.close()
#         cls.driver.quit()
#
#
