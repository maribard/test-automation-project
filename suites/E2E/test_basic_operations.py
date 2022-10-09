import unittest
from datetime import date

from selenium import webdriver

from handlers.basic_handler import *

CHROME = 'C:/Users/m.bardyn/webdriver/chromedriver.exe'
URL = "http://qalab.pl.tivixlabs.com/"
concurrent_date = date.today()
unexpected_msgs = ['KeyError', 'Page not found', 'Exception']


class Basic_tests(unittest.TestCase):

    car_rent_handler = None

    def setUp(self):
        driver = webdriver.Chrome(CHROME)
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.set_page_load_timeout(8)
        driver.get(URL)

        self.car_rent_handler = BasicHandler(driver=driver)

    def tearDown(self):
        self.car_rent_handler.close_sesion()
        time.sleep(10)

    def test_a_verify_that_user_is_able_to_search_cars(self):
        self.car_rent_handler.is_displayed('#search_form')
        self.car_rent_handler.find_selectable_element_and_click(css_selector='#country', wanted_option='Poland')
        self.car_rent_handler.find_selectable_element_and_click(css_selector='#city', wanted_option='Cracow')
        self.car_rent_handler.find_and_fill_date_box('#pickup', concurrent_date.day, concurrent_date.month,
                                                      concurrent_date.year)
        self.car_rent_handler.find_and_fill_date_box('#dropoff', concurrent_date.day + 3, concurrent_date.month,
                                                      concurrent_date.year)
        self.car_rent_handler.click('.btn')
        self.car_rent_handler.is_displayed('#search-results')

    def test_b_verify_that_user_is_able_to_see_cars_details(self):
        self.car_rent_handler.find_selectable_element_and_click(css_selector='#country', wanted_option='Poland')
        self.car_rent_handler.find_selectable_element_and_click(css_selector='#city', wanted_option='Cracow')
        self.car_rent_handler.find_and_fill_date_box('#pickup', concurrent_date.day, concurrent_date.month,
                                                      concurrent_date.year)
        self.car_rent_handler.find_and_fill_date_box('#dropoff', concurrent_date.day + 3, concurrent_date.month,
                                                      concurrent_date.year)
        self.car_rent_handler.click('.btn')
        self.car_rent_handler.is_displayed('#search-results')

        self.car_rent_handler.find_table_and_rent_a_car(css_selector_table='#search-results > tbody:nth-child(2)')
        self.car_rent_handler.is_displayed('.card')

    def test_c_verify_that_user_is_able_to_rent_car_and_provide_personal_data(self):
        self.car_rent_handler.find_selectable_element_and_click(css_selector='#country', wanted_option='Poland')
        self.car_rent_handler.find_selectable_element_and_click(css_selector='#city', wanted_option='Cracow')
        self.car_rent_handler.find_and_fill_date_box('#pickup', concurrent_date.day, concurrent_date.month,
                                                      concurrent_date.year)
        self.car_rent_handler.find_and_fill_date_box('#dropoff', concurrent_date.day + 3, concurrent_date.month,
                                                      concurrent_date.year)
        self.car_rent_handler.click('.btn')
        self.car_rent_handler.is_displayed('#search-results')

        self.car_rent_handler.find_table_and_rent_a_car(css_selector_table='#search-results > tbody:nth-child(2)')
        self.car_rent_handler.is_displayed('.card')
        self.car_rent_handler.click('.btn')
        self.car_rent_handler.is_displayed('#content')

        self.car_rent_handler.find_and_fill_test_box(css_selector_test_box='#name', text='Mariusz')
        self.car_rent_handler.find_and_fill_test_box(css_selector_test_box='#last_name', text='Bardyn')
        self.car_rent_handler.find_and_fill_test_box(css_selector_test_box='#card_number', text='1234567891011213')
        self.car_rent_handler.find_and_fill_test_box(css_selector_test_box='#email', text='maribard@gmail.com')
        self.car_rent_handler.click('.btn')

        page_source = self.car_rent_handler.get_page_source()
        self.car_rent_handler.verify_if_there_is_no_unexpected_msg(page=page_source, unexpec_msgs=unexpected_msgs)


