# -*- coding: cp1251 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OARegistrationElement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://develop.starline.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_o_a_registration_element(self):
        driver = self.driver
        driver.get(self.base_url + "/")
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
        driver.find_element_by_xpath("//div[@id='register']/span[2]").click()
        time.sleep(1)
        try: self.assertEqual(u"�����������", driver.find_element_by_css_selector("h4").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        try: self.assertRegexpMatches(driver.find_element_by_css_selector("h5").text, r"� ��� ���� ����� ���������")
        try: self.assertEqual(u"� ��� ���� ����� ���������?", driver.find_element_by_css_selector("h5").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("img").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"����� ��������� ������������ ������ � �������������� � GSM-�������� M21, M31 � M32", driver.find_element_by_xpath("//form[@id='check-card-form']/div/div/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"��� �����", driver.find_element_by_id("card-no").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"���� �����", driver.find_element_by_id("card-yes").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//form[@id='check-card-form']/div/span").click()
        time.sleep(1)
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
