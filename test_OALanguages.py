# -*- coding: cp1251 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OALanguages(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://develop.starline.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_o_a_languages(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try: self.assertEqual(u"Спутниковый\nохранно-мониторинговый\nсервис", driver.find_element_by_css_selector("h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Демо-вход", driver.find_element_by_xpath("//div[@id='demo']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Вход", driver.find_element_by_id("login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Регистрация", driver.find_element_by_xpath("//div[@id='register']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a > span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("a > span").click()
        try: self.assertEqual(u"русский", driver.find_element_by_css_selector("a > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("english", driver.find_element_by_xpath("//div[@id='language-switch']/div/div[2]/a/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("italian", driver.find_element_by_xpath("//div[@id='language-switch']/div/div[3]/a/span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='language-switch']/div/div[2]/a/span").click()
        try: self.assertEqual("Satellite Security and\nMonitoring Service", driver.find_element_by_css_selector("h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Try demo", driver.find_element_by_xpath("//div[@id='demo']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Вход", driver.find_element_by_id("login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Registration", driver.find_element_by_xpath("//div[@id='register']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a > span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("a > span").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a > span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='language-switch']/div/div[2]/a/span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='language-switch']/div/div[3]/a/span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='language-switch']/div/div[3]/a/span").click()
        try: self.assertEqual("Servizio satellitare di antifurto e monitoraggio", driver.find_element_by_css_selector("h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Demo-accesso", driver.find_element_by_xpath("//div[@id='demo']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Вход", driver.find_element_by_xpath("//div[@id='login']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("Registrazione", driver.find_element_by_xpath("//div[@id='register']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a > span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_css_selector("a > span").click()
        try: self.assertTrue(self.is_element_present(By.CSS_SELECTOR, "a > span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='language-switch']/div/div[2]/a/span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertTrue(self.is_element_present(By.XPATH, "//div[@id='language-switch']/div/div[3]/a/span"))
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.find_element_by_xpath("//div[@id='language-switch']/div/div[2]/a/span").click()
        try: self.assertEqual(u"Спутниковый\nохранно-мониторинговый\nсервис", driver.find_element_by_css_selector("h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Демо-вход", driver.find_element_by_xpath("//div[@id='demo']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Вход", driver.find_element_by_id("login").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Регистрация", driver.find_element_by_id("register").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"русский", driver.find_element_by_css_selector("a > span").text)
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
