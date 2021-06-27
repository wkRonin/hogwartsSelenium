# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 15:00
# @Author  : wkRonin
# @File    :test_add_member.py
import pytest
from homework0627.po.main_page import MainPage


class TestAddMember:
    def setup(self):
        self.main = MainPage()

    def teardown(self):
        pass

    @pytest.mark.parametrize("name,contact_id,mail", [
        ("张一", "0627", "qwefdsf@qq.com"),
        ("张二", "0628", "qwefdsf1@qq.com")
    ])
    def test_add_member(self, name, contact_id, mail):
        # 链式调用
        result = self.main.goto_contact().click_add_member().\
            edit_member(name, contact_id, mail).get_member_name()
        print(result)
        assert name in result
