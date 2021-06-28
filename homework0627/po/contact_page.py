# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 14:59
# @Author  : wkRonin
# @File    :contact_page.py
import time
from selenium.webdriver.common.by import By
from homework0627.po.add_member_page import AddMemberPage
from homework0627.po.basepage import BasePage
from homework0627.po.contact_deptment_page import AddDeptPage


class ContactPage(BasePage):

    _ADDMEMBER = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")
    _MEMBERNAMES = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _ADD = (By.CSS_SELECTOR, "div.member_colLeft_top.member_colLeft_top_BorderBottom > a")
    _ADDDEPT = (By.CSS_SELECTOR, ".js_create_party")
    _DEPTNAMES = (By.CSS_SELECTOR, 'ul[role="group"] li[role="treeitem"] .jstree-anchor')

    def click_add_member(self):
        """
        点击添加成员
        :return:返回添加成员页面
        """
        self.wait_for_click(self._ADDMEMBER)
        return AddMemberPage(self.driver)

    def get_member_name(self):
        """
        获取成员信息
        :return: 成员姓名列表
        """
        time.sleep(1)
        name_list = []
        eles = self.finds(*self._MEMBERNAMES)
        for value in eles:
            name_list.append(value.get_attribute("title"))
        return name_list

    def click_add_dept(self):
        """
        点击+号下的添加部门
        :return:返回添加部门页面
        """
        # 点击➕
        self.wait_for_click(self._ADD)
        # 点击添加部门
        self.find_and_click(*self._ADDDEPT)
        return AddDeptPage(self.driver)

    def get_dept_name(self):
        """
        获取部门信息
        :return: 部门名称列表
        """
        time.sleep(1)
        name_list = []
        eles = self.finds(*self._DEPTNAMES)
        for value in eles:
            name_list.append(value.text)
        return name_list



