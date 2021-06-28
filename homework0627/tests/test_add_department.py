# -*- coding: utf-8 -*-
# @Time    : 2021/6/28 22:22
# @Author  : wkRonin
# @File    :test_add_department.py
import pytest

from homework0627.po.main_page import MainPage


class TestAddDepartment:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name", ["testdept5", "testdept6"])
    def test_add_department(self, name):
        result = self.main.goto_contact().click_add_dept().edit_department(name).get_dept_name()
        print(result)
        assert name in result
