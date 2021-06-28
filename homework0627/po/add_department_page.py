# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 23:05
# @Author  : wkRonin
# @File    :add_department_page.py
from selenium.webdriver.common.by import By

from homework0627.po.basepage import BasePage



class AddDeptPage(BasePage):

    _DEPTNAME = (By.CSS_SELECTOR, "form > div:nth-child(1) > input")
    _TODEPT = (By.CSS_SELECTOR, "form > div:nth-child(3) > a")
    _ROOTDEPT = (By.ID, "1688851276809568_anchor")
    _SUBMITDEPT = (By.CSS_SELECTOR, "div.qui_dialog_foot.ww_dialog_foot > a.qui_btn.ww_btn.ww_btn_Blue")

    def edit_department(self, dept_name):
        """
        添加部门信息
        :return:返回通讯录页面
        """
        from homework0627.po.contact_page import ContactPage
        # 输入部门名称
        self.find(*self._DEPTNAME).send_keys(dept_name)
        # 点击所属部门
        self.find_and_click(*self._TODEPT)
        # 点击根部门
        self.finds(*self._ROOTDEPT)[1].click()
        # 点击确定
        self.find_and_click(*self._SUBMITDEPT)
        return ContactPage(self.driver)
