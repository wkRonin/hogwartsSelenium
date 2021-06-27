# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 14:59
# @Author  : wkRonin
# @File    :contact_page.py
import time
from selenium.webdriver.common.by import By
from homework0627.po.add_member_page import AddMemberPage
from homework0627.po.basepage import BasePage


class ContactPage(BasePage):
    _ADDMEMBER = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _NAMES = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")

    # 点击添加成员
    def click_add_member(self):
        self.wait_for_click(self._ADDMEMBER)
        return AddMemberPage(self.driver)

    # 获取成员信息，进行返回
    def get_member_name(self):
        time.sleep(1)
        name_list = []
        eles = self.finds(*self._NAMES)
        for value in eles:
            name_list.append(value.get_attribute("title"))
        return name_list

