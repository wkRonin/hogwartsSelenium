# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 14:59
# @Author  : wkRonin
# @File    :contact_page.py
import logging
import time

import allure
from selenium.webdriver.common.by import By
from homework0627.po.add_member_page import AddMemberPage
from homework0627.po.basepage import BasePage
from homework0627.po.add_department_page import AddDeptPage


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
        with allure.step("点击添加成员"):
            self.wait_for_click(self._ADDMEMBER)
            logging.info("点击添加成员")
        return AddMemberPage(self.driver)

    def get_member_name(self):
        """
        获取成员信息
        :return: 成员姓名列表
        """
        time.sleep(1)
        name_list = []
        with allure.step('获取成员信息'):
            eles = self.finds(*self._MEMBERNAMES)
            for value in eles:
                name_list.append(value.get_attribute("title"))
            logging.info(f'获取成员信息: {name_list}')
        return name_list

    def click_add_dept(self):
        """
        点击+号下的添加部门
        :return:返回添加部门页面
        """
        with allure.step('点击+号下的添加部门'):
            # 点击➕
            self.wait_for_click(self._ADD)
            logging.info('点击➕')
            # 点击添加部门
            self.find_and_click(*self._ADDDEPT)
            logging.info('点击添加部门')
        return AddDeptPage(self.driver)

    def get_dept_name(self):
        """
        获取部门信息
        :return: 部门名称列表
        """
        time.sleep(1)
        name_list = []
        with allure.step('获取部门信息'):
            eles = self.finds(*self._DEPTNAMES)
            for value in eles:
                name_list.append(value.text)
            logging.info(f'获取部门信息: {name_list}')
        return name_list



