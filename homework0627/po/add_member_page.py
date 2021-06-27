# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 15:00
# @Author  : wkRonin
# @File    :add_member_page.py

from selenium.webdriver.common.by import By
from homework0627.po.basepage import BasePage


class AddMemberPage(BasePage):
    _NAME = (By.ID, "username")
    _ACCTID = (By.ID, "memberAdd_acctid")
    _MAIL = (By.ID, "memberAdd_mail")
    _SAVE = (By.CSS_SELECTOR, ".js_btn_save")

    # 添加成员信息
    def edit_member(self, name, contact_id, mail):
        # 局部导入，解决循环导入问题
        from homework0627.po.contact_page import ContactPage
        self.find(*self._NAME).send_keys(name)
        self.find(*self._ACCTID).send_keys(contact_id)
        self.find(*self._MAIL).send_keys(mail)
        self.find_and_click(*self._SAVE)
        return ContactPage(self.driver)




