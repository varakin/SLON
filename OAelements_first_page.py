# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OAElementsFirstPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://develop.starline.ru/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_o_a_elements_first_page(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        try: self.assertEqual("StarLine=", driver.find_element_by_id("logo").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Спутниковый\nохранно-мониторинговый\nсервис", driver.find_element_by_css_selector("h1").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Демо-вход", driver.find_element_by_xpath("//div[@id='demo']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Вход", driver.find_element_by_xpath("//div[@id='login']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Регистрация", driver.find_element_by_xpath("//div[@id='register']/span[2]").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"Загрузите StarLine на Ваш смартфон:", driver.find_element_by_css_selector("div.table-cell.title > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.form-icon.app-store").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.form-icon.google-play").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("span.form-icon.windows-phone").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"© 2015 НПО \"СтарЛайн\"", driver.find_element_by_css_selector("#footer-copyright > span").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"каталог устройств StarLine", driver.find_element_by_link_text(u"каталог устройств StarLine").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual(u"как купить и установить", driver.find_element_by_link_text(u"как купить и установить").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("a.social-icon.vk").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("a.social-icon.tw").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("a.social-icon.fb").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("a.social-icon.lj").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("a.social-icon.yt").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        try: self.assertEqual("", driver.find_element_by_css_selector("a.social-icon.ig").text)
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
