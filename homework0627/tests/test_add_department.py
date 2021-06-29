# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 22:22
# @Author  : wkRonin
# @File    :test_add_department.py
import logging
import os
import shutil

import allure
import pytest

from homework0627.po.main_page import MainPage


@allure.feature('企业微信添加部门')
class TestAddDepartment:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name", ["testdept9"])
    @allure.story("通讯录测试")
    @allure.title("添加部门并保存成功")
    def test_add_department(self, name):
        result = self.main.goto_contact().click_add_dept().edit_department(name).get_dept_name()
        self.main.save_screenshot('img/deptimg.png', '添加部门截图')
        logging.info(f'断言{name}是否在{result}中')
        assert name in result
