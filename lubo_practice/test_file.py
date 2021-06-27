# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 12:33
# @Author  : wkRonin
# @File    :test_file.py
import time

import pytest

from base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id('stfile').send_keys(r"D:\pycharmproject\hogwartsSelenium\img\baidu.png")
        time.sleep(5)
