# -*- coding: cp1251 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OACheckEnterActivation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://develop.starline.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_o_a_check_enter_activation(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("login").click()
        try: self.assertEqual(u"Для первого входа в систему и активации Вашего устройства используйте Логин и Пароль напечатанные на Карте", driver.find_element_by_xpath("//div[@id='check-card-notice']/div/div/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Карта активации находится в коробке с устройством StarLine. Поставляется с сигнализациями и GSM-модулями M21, M31, M32", driver.find_element_by_css_selector("div.form-input-advice.text-blue").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("input[type=\"checkbox\"]").click()
        driver.find_element_by_xpath("//form[@id='login-form']/div/span").click()
        try: self.assertEqual(u"Демо-вход", driver.find_element_by_id("demo").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Вход", driver.find_element_by_xpath("//div[@id='login']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Регистрация", driver.find_element_by_xpath("//div[@id='register']/span[2]").text)
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
