# -*- coding: cp1251 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Qwerty(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://develop.starline.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_qwerty(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//div[@id='login']/span[2]").click()
        try: self.assertEqual(u"Вход", driver.find_element_by_css_selector("#login-form > div.content > h4").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_name("LoginForm[login]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_name("LoginForm[pass]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"запомнить меня", driver.find_element_by_css_selector("#login-form > div.content > div.checkbox > label").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Войти", driver.find_element_by_css_selector("button.form-button.enter").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertRegexpMatches(driver.find_element_by_link_text(u"Забыли пароль?").text, r"^exact:Забыли пароль[\s\S]$")
#        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"пользовательским соглашением", driver.find_element_by_css_selector("em").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
