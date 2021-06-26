# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 11:16
# @Author  : wkRonin
# @File    :test_wework.py
import logging
import time
import allure

import yaml
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

fake = Faker("zh_CN")


@allure.feature("企业微信添加成员")
class TestWework:

    # def test_save_cookies(self, multiplex_driver):
    #     # 手动登录并提取cookie
    #     multiplex_driver.get("https://work.weixin.qq.com/wework_admin/frame")
    #     multiplex_driver.find_element_by_id("menu_contacts").click()
    #     my_cookies = multiplex_driver.get_cookies()
    #
    #     # 保存cookie到cookies.yaml文件
    #     with open("cookies/data.yaml", "w", encoding="UTF-8") as f:
    #         yaml.dump(my_cookies, f)
    #
    # def test_read_cookies(self, read_cookies):
    #     logging.info(f'读取的cookie: {read_cookies}')
    @allure.story("通讯录测试")
    @allure.title("添加成员并保存成功")
    def test_add_members(self, chrome_driver, read_cookies):
        chrome_driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        cookies = read_cookies
        for cookie in cookies:
            chrome_driver.add_cookie(cookie)
        logging.info('获取cookie成功')

        # 读取cookie后进入首页
        with allure.step('进入首页'):
            chrome_driver.get("https://work.weixin.qq.com/wework_admin/frame")

        # 点击通讯录菜单
        with allure.step('进入通讯录菜单'):
            menu_contacts_button = chrome_driver.find_element_by_id('menu_contacts')
            menu_contacts_button.click()
            time.sleep(1)

        # 点击‘添加成员’按钮
        with allure.step('进入成员添加页面'):
            add_member_button = chrome_driver.find_element_by_css_selector('div:nth-child(1) > a.qui_btn.ww_btn.js_add_member')
            add_member_button.click()
            time.sleep(3)

        with allure.step('录入成员信息'):
            # 输入姓名
            username_input = chrome_driver.find_element_by_id('username')
            username = fake.name_male()
            logging.info(f"输入的姓名为： {username}")
            username_input.send_keys(f"{username}")

            # 输入别名
            aliasname_input = chrome_driver.find_element_by_id("memberAdd_english_name")
            logging.info(f"输入的别名为： {username}")
            aliasname_input.send_keys(f"{username}")

            # 输入账号
            acctid_input = chrome_driver.find_element_by_id("memberAdd_acctid")
            acctid = fake.random_number(digits=8)
            logging.info(f"输入的账号为： {acctid}")
            acctid_input.send_keys(f"{acctid}")

            # 输入手机号
            phone_input = chrome_driver.find_element_by_id("memberAdd_phone")
            phone = fake.phone_number()
            logging.info(f"输入的手机号为： {phone}")
            phone_input.send_keys(f"{phone}")

            # 输入座机
            telephone_input = chrome_driver.find_element_by_id("memberAdd_telephone")
            telephone = fake.random_number(digits=8)
            logging.info(f"输入的座机为： {telephone}")
            telephone_input.send_keys(f"{telephone}")

            # 输入邮箱
            email_input = chrome_driver.find_element_by_id("memberAdd_mail")
            email = fake.email()
            logging.info(f'输入的邮箱为： {email}')
            email_input.send_keys(f'{email}')

            # 输入地址
            address_input = chrome_driver.find_element_by_id("memberEdit_address")
            address = fake.street_address()
            logging.info(f'输入的地址为： {address}')
            address_input.send_keys(f'{address}')

            # 输入职务
            title_input = chrome_driver.find_element_by_id("memberAdd_title")
            title = fake.job()
            logging.info(f"输入的职务为： {title}")
            title_input.send_keys(f'{title}')

            # 点击保存按钮
            save_button = chrome_driver.find_element_by_css_selector('div:nth-child(3) > a.qui_btn.ww_btn.js_btn_save')
            save_button.click()
            time.sleep(1)

        # 列表截图
        with allure.step('成员添加成功截图'):
            chrome_driver.save_screenshot("img/success.png")
            allure.attach.file('img/success.png', '成员添加成功截图')

        # 根据手机号断言列表是否存在添加的成员(手机号有唯一性)
        with allure.step('断言成员是否在通讯录列表中'):
            member_list = chrome_driver.find_element_by_id("member_list")
            try:
                assert 'phone' in member_list.text
                logging.info(f'添加的成员：{username},手机号：{phone}...存在列表中')
            except Exception as e:
                logging.info(e)




