# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 11:32
# @Author  : wkRonin
# @File    :conftest.py

import logging
import pytest
import yaml
from selenium import webdriver


@pytest.fixture(scope='session')
def chrome_driver():
    logging.info("初始化chrome driver")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    logging.info('退出Chrome driver')
    driver.quit()


@pytest.fixture(scope='class')
def multiplex_driver():
    logging.info("初始化复用谷歌页面")
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    yield driver


@pytest.fixture(scope='class')
def read_cookies():
    with open("cookies/data.yaml", encoding="UTF-8") as f:
        local_cookies = yaml.safe_load(f)
    return local_cookies

