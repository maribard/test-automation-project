from datetime import datetime
import random
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class BasicHandler(object):


    def __init__(self, driver):
        self.driver = driver

    def find_selectable_element_and_click(self, css_selector, wanted_option):
        """
        This method allow to find selectale element by css_selector and choose wanted option

        :param css_selector: selectable element
        :param option: wanted option
        :return:
        """
        select_country = Select(self.driver.find_element(By.CSS_SELECTOR, css_selector))
        for option in select_country.options:
            if option.text == wanted_option:
                option.click()
                return

        raise NoSuchElementException(f"Element not found: {wanted_option}")

    def find_and_fill_date_box(self, css_selector, day, month, year):
        """
        This method allow to find element by css_selector and fill it

        :param css_selector: css_selector
        :param day: day
        :param montch: montch
        :param year: year
        :return:
        """
        try:
            date_box_from = self.driver.find_element(By.CSS_SELECTOR, css_selector)
            date_box_from.send_keys("{}{}{}".format(day, month, year))
            date_box_from.click()
        except NoSuchElementException:
            return False

    def is_displayed(self, css_selector):
        """
        This method allow to find element by css_selector and fill it

        :param css_selector:
        :return:
        """
        try:
            return self.driver.find_element(By.CSS_SELECTOR, css_selector).is_displayed()
        except NoSuchElementException:
            return False

    def find_table_and_rent_a_car(self, css_selector_table=None, css_selector_car=None):
        """
        This method allow to find table and rent random car or rent specific car

        :param css_selector_table: css_selector_table
        :param css_selector_car: css_selector_car
        :return:
        """
        if css_selector_car is not None:
            self.click(css_selector_car)
        else:
            table = self.driver.find_element(By.CSS_SELECTOR, css_selector_table)
            len_rows = len(table.find_elements(By.CSS_SELECTOR, 'tr'))
            rand_rows = random.randint(1, len_rows)
            self.driver.find_element(By.CSS_SELECTOR, '#search-results > tbody:nth-child(2) > tr:nth-child({}) > '
                                                      'td:nth-child(7) > a:nth-child(1)'.format(rand_rows)).click()

    def find_and_fill_test_box(self, css_selector_test_box, text):
        try:
            text_box_from = self.driver.find_element(By.CSS_SELECTOR, css_selector_test_box)
            text_box_from.send_keys("{}".format(text))
        except NoSuchElementException:
            return False

    def click(self, css_selector):
        try:
            return self.driver.find_element(By.CSS_SELECTOR, css_selector).click()
        except NoSuchElementException:
            return False

    def get_page_source(self):
        return self.driver.page_source

    def verify_if_there_is_no_unexpected_msg(self, page, unexpec_msgs):
        date_now = datetime.now()
        msg = list()
        for unexpected in unexpec_msgs:
            if unexpected in page:
                msg.append(unexpected)
                self.driver.save_screenshot(str(date_now) + '_image_error.png')
        if msg:
            raise AssertionError(f'found unexpected msgs: {msg}')

    def close_sesion(self):
        self.driver.quit()
        time.sleep(4)




