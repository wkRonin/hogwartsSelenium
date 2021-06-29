# -*- coding: utf-8 -*-
# @Time    : 2021/6/29 22:23
# @Author  : wkRonin
# @File    :run.py
import logging
import os
import shutil

import pytest

if __name__ == '__main__':
    if os.path.exists('report/'):
        shutil.rmtree(path='report/')
    pytest.main(
        args=[
            './test_add_department.py',
            '-vs']
            )
    # # 自动以服务形式打开报告
    # print('自动以服务形式打开报告')
    logging.info('自动以服务形式打开报告')

    os.system('allure serve ./report -o ./result  --clean')

    # 本地生成报告
    # os.system('allure generate ./report/data -o report/html --clean')