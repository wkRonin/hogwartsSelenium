# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 16:06
# @Author  : wkRonin
# @File    :basepage.py
import logging

import allure
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver_base: WebDriver = None):
        # 避免driver重复初始化
        if driver_base is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
            logging.info("实例化driver")
        else:
            self.driver = driver_base

    def find(self, by, locator):
        ele = self.driver.find_element(by, locator)
        return ele

    def finds(self, by, locator):
        eles = self.driver.find_elements(by, locator)
        return eles

    def find_and_click(self, by, locator):
        ele = self.driver.find_element(by, locator)
        ele.click()

    def wait_for_click(self, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        element.click()
        return element

    def save_screenshot(self, path, stepname):
        """
        allure报告截图步骤
        :param path: 截图保存的路径
        :param stepname: 步骤名称
        :return:
        """
        with allure.step(stepname):
            self.driver.save_screenshot(path)
            allure.attach.file(path, stepname)

