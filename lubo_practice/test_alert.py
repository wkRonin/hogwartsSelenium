# -*- coding: utf-8 -*-
# @Time    : 2021/6/27 13:09
# @Author  : wkRonin
# @File    :test_alert.py
import time

import pytest
from selenium.webdriver import ActionChains

from base import Base


class TestAlert(Base):
    def test_alert(self):
        """
        打开网页https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable
        操作窗口右侧页面，将元素1拖到元素2
        点击弹框中的确定
        点击‘点击运行’
        :return:
        """
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        time.sleep(3)
        print("点击 alert 确认")
        self.driver.switch_to.alert.accept()
        # 切换回默认frame
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()
        time.sleep(3)
