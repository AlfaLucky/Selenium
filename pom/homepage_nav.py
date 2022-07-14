from base.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List


class HomePageNav(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__nav_links: str = '#snail-trail-container>li'
        self.NAV_LINK_TEXT = 'BOYS,GIRLS,BABY,WOMEN,MEN,HOME,BRANDS,SPORTS,SUMMER SHOP'

    def get_nav_links(self) -> List[WebElement]:
        """Returns a list of web elements in the nav bar"""
        return self.are_visible('css', self.__nav_links, 'Header Navigation Links')

    def get_nav_links_text(self) -> str:
        """Creates and writes an object to a new sheet, Returns the text as a string"""
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(elements=nav_links)
        return ",".join(nav_links_text)
