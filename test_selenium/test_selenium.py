# -*- coding: utf-8 -*-
# @Time    : 2021/6/23 22:04
# @Author  : wkRonin
# @File    :test_selenium.py
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaidu():
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "kw").send_keys("霍格沃兹测试学院")
        time.sleep(2)
        self.driver.find_element(By.ID, "su").click()
        time.sleep(3)


def test_login():
    # 复用页面获取cookie
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    driver.find_element_by_id("menu_contacts").click()
    cookies = driver.get_cookies()
    with open("data.yaml", "w", encoding="UTF-8") as f:
        yaml.dump(cookies, f)
    # print(driver.get_cookies())


# cookie放在代码中
def test_wework():
    # 打开新的浏览器，设置cookie,跳过扫码登录
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688851276809557'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688851276809557'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '9254732150'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325059462369'}, {'domain': '.qq.com', 'expiry': 1624761400, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1575740796.1624626247'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'xmp_T4veBaAXMxwU8bIT-T0oRzNJj_mbIZTOqe_tRVY_bVV9_roaPWQLbvLNki1W'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a2859385'}, {'domain': '.qq.com', 'expiry': 1624675047, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '18723206132186409'}, {'domain': 'work.weixin.qq.com', 'expiry': 1624705336, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '131n28a'}, {'domain': '.work.weixin.qq.com', 'expiry': 1627267003, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1687747000, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1597091739.1624626247'}, {'domain': '.qq.com', 'expiry': 1938261871, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '29fb0979f3967c20'}, {'domain': '.work.weixin.qq.com', 'expiry': 1656162167, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'a2756d6148e81af89959197e0448d0d2b61ab95c3b8c7865d497e4375d05745a'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'DQQ9OU3+Rc'}, {'domain': '.qq.com', 'expiry': 1624718419, 'httpOnly': False, 'name': 'uid', 'path': '/', 'secure': False, 'value': '196726702'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 1654415786, 'httpOnly': False, 'name': 'Qs_pv_323937', 'path': '/', 'secure': False, 'value': '394011312332497300'}, {'domain': '.qq.com', 'expiry': 1625578287, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '963072073'}, {'domain': '.qq.com', 'expiry': 1654415786, 'httpOnly': False, 'name': 'Qs_lvt_323937', 'path': '/', 'secure': False, 'value': '1622879786'}, {'domain': '.qq.com', 'expiry': 1654415800, 'httpOnly': False, 'name': 'eas_sid', 'path': '/', 'secure': False, 'value': 'i1j6y242C8I7z9I8l070B2F1t7'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'bC6iTij6NPwJW0apXnv8n2en-CAxM_VpryWxxjqJbCYDhwWViqaus41FeioEbZT-UaoA3JeNoPGg5bolvMz2bL5Y_HWWSzmmErmu1DQpNborhh30epJb27C74_yW1hSLcnI1Ai_okfTfM4J2ZeWBkQeA_Fbjewq8x2g6UaD4CT05qAUcD4Rsg6_0F41Nq9SZCqzXKkladdWMBPUxL3qvjLeHuSTQCUpuVMmuWYoeg5HnUHTAsZJfs8iuzub-sn3DKYFfb_4N3OVsdduS3OQ7Bg'}, {'domain': '.work.weixin.qq.com', 'expiry': 1656210011, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1624626247,1624628727,1624674012'}]
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    time.sleep(5)
    driver.quit()


# 从yaml文件读取cookie
def test_load_cookie():
    driver = webdriver.Chrome()
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
    with open("data.yaml", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
    for cookie in yaml_data:
        driver.add_cookie(cookie)
    driver.get("https://work.weixin.qq.com/wework_admin/frame")
    time.sleep(5)
    driver.quit()
