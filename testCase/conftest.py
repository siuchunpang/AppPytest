# -*- encoding=utf8 -*-

__author__ = "xsl"

import pytest
from tools.tool import *
from airtest.core.api import *
from airtest.report.report import simple_report


@pytest.fixture(scope="module")
def ini():

    # file_name = os.environ.get('PYTEST_CURRENT_TEST').split(':')[0].split('/')[1].split('.')[0]
    # logging.info("用例文件名称：%s" % file_name)
    # global air_log
    # air_log = os.path.join(air_log_path, file_name + "_" + now)
    # os.makedirs(air_log)
    # 初始化应用
    start_app("com.fdage.eight")
    sleep(10)

    yield
    # 生成报告
    now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    simple_report(__file__, logpath=air_log_path, output=air_report_path + "\\air_report_" + str(now) + ".html")
    stop_app("com.fdage.eight")


# 1. 调用钩子方法, item 参数这里不用
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport():
#     print('------------------------------------')
#
#     # 2. 获取钩子方法的调用结果
#     result = yield
#     print('钩子方法的执行结果', result)
#
#     # 3. 从钩子方法的调用结果中获取测试报告
#     report = result.get_result()
#
#     if report.when == "call" and report.passed:
#         print('从结果中获取测试报告：', report)
#         print('从报告中获取 nodeid：', report.nodeid)
#         print('从报告中获取调用步骤：', report.when)
#         print('从报告中获取执行结果：', report.outcome)

