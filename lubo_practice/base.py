# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 11:25
# @Author  : wkRonin
# @File    :base.py
import os

from selenium import webdriver


class Base:
    def setup(self):
        # 使用os模块的getenv方法来获取声明环境变量browser
        browser = os.getenv("browser")
        # 判断browser的值
        if browser == "headless":
            self.driver = webdriver.PhantomJS()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()
