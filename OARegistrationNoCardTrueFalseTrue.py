# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OARegistrationNoCardTrueFalseTrue(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://develop.starline.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_o_a_registration_no_card_true_false_true(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try: self.assertEqual(u"����-����", driver.find_element_by_xpath("//div[@id='demo']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"����", driver.find_element_by_xpath("//div[@id='login']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"�����������", driver.find_element_by_xpath("//div[@id='register']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='register']/span[2]").click()
        try: self.assertEqual(u"�����������", driver.find_element_by_css_selector("h4").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"����� ��������� ������������ ������ � �������������� � GSM-�������� M21, M31 � M32", driver.find_element_by_xpath("//form[@id='check-card-form']/div/div/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_id("card-no").click()
        try: self.assertEqual(u"�����������", driver.find_element_by_css_selector("h4").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_name("email").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_name("password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_name("passwordConfirmation").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"� ���� ����� SIM-����� ����� ����������", driver.find_element_by_id("haveGsm").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("varakin.1@mail.ru")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("654321")
        driver.find_element_by_name("passwordConfirmation").clear()
        driver.find_element_by_name("passwordConfirmation").send_keys("123456")
        driver.find_element_by_name("LoginForm[rememberMe]").click()
        driver.find_element_by_css_selector("button.form-button.register").click()
        try: self.assertEqual(u"��������� ������ �� ���������.", driver.find_element_by_css_selector("h3").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("div.error > div").click()
        try: self.assertEqual("", driver.find_element_by_name("email").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_name("password").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_name("passwordConfirmation").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//form[@id='registration-form']/div/span").click()
        try: self.assertEqual(u"����-����", driver.find_element_by_xpath("//div[@id='demo']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"����", driver.find_element_by_xpath("//div[@id='login']/span[2]").text)
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
