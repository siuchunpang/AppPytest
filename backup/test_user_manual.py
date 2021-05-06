# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_UserManual(ini):
    # 测试用例：用户手册&快速上手

    # 用户手册
    poco("com.fdage.eight:id/iv_my").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_user_help", text="用户手册").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_titlebar_title", text="用户手册").wait_for_appearance(5)
    logging.info("打开用户手册")

    # 快速上手
    poco("com.fdage.eight:id/tv_right", text="快速上手").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_titlebar_title", text="快速上手").wait_for_appearance(5)
    sleep(1.0)
    poco("com.fdage.eight:id/tv_right", text="用户手册").wait_for_appearance(5)
    sleep(1.0)
    poco("com.fdage.eight:id/videoView").swipe([-0.8821, 0.0091])
    sleep(2.0)
    poco("com.fdage.eight:id/iv_left").click()
    sleep(1.0)
    poco("com.fdage.eight:id/iv_left").click()
    sleep(1.0)
    poco("com.fdage.eight:id/iv_my").wait_for_appearance(10)


if __name__ == '__main__':
    pytest.main()
