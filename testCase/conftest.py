# -*- encoding=utf8 -*-

__author__ = "xsl"

import pytest
from tools.tool import *
from airtest.core.api import *
from airtest.report.report import simple_report


@pytest.fixture(scope="module")
def ini():
    # 初始化应用
    start_app("com.fdage.eight")
    sleep(10)

    yield
    # 生成报告
    now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    simple_report(__file__, logpath=air_log_path, output=air_report_path + "\\air-report" + str(now) + ".html")
    stop_app("com.fdage.eight")
