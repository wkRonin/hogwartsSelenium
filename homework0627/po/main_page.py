# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 14:59
# @Author  : wkRonin
# @File    :main_page.py
import logging

import allure
from selenium.webdriver.common.by import By
from homework0627.po.basepage import BasePage
from homework0627.po.contact_page import ContactPage


class MainPage(BasePage):
    _CONTACT = (By.ID, "menu_contacts")

    # 跳转至通讯录页面
    def goto_contact(self):
        with allure.step('跳转至通讯录页面'):
            self.find_and_click(*self._CONTACT)
            logging.info('跳转至通讯录页面')
        return ContactPage(self.driver)

