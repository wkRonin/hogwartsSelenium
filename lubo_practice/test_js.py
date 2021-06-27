# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 11:16
# @Author  : wkRonin
# @File    :test_js.py
import time

import pytest

from base import Base


class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        """
        滑动到浏览器底部或者顶部
        :return:
        """
        self.driver.get("https://baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        # 返回需要点击的元素
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        # 移动到底部
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        # 点击下一页
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        time.sleep(3)
        # 获取网页title以及性能数据
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        # 移除readonly属性
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        time.sleep(1)
        # 给日期赋值
        self.driver.execute_script('document.getElementById("train_date").value="2021-07-22"')
        time.sleep(3)
        print(self.driver.execute_script('return document.getElementById("train_date").value'))
