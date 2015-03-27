# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OACheckEnterTrueTrue(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://develop.starline.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_o_a_check_enter_true_true(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("//div[@id='login']/span[2]").click()
        driver.find_element_by_name("LoginForm[login]").clear()
        driver.find_element_by_name("LoginForm[login]").send_keys("varakin.1@mail.ru")
        driver.find_element_by_name("LoginForm[pass]").clear()
        driver.find_element_by_name("LoginForm[pass]").send_keys("123456")
        driver.find_element_by_css_selector("button.form-button.enter").click()
        try: self.assertEqual(u"��������� ����������", driver.find_element_by_link_text(u"��������� ����������").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"����", driver.find_element_by_link_text(u"����").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"����", driver.find_element_by_link_text(u"����").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"�����", driver.find_element_by_link_text(u"�����").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_link_text(u"�����").click()
        try: self.assertEqual("StarLine=", driver.find_element_by_id("logo").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"�����������\n�������-��������������\n������", driver.find_element_by_css_selector("h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"����-����", driver.find_element_by_xpath("//div[@id='demo']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"����", driver.find_element_by_id("login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"�����������", driver.find_element_by_xpath("//div[@id='register']/span[2]").text)
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
