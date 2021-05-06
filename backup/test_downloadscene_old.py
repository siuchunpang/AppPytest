# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_downloadscene_old(ini):
    # 登录账号
    connect_wifi()

    # 登录
    logging.info("开始登录")
    poco("com.fdage.eight:id/tv_user_name").click()
    sleep(1)
    poco("com.fdage.eight:id/et_phone").set_text("13138102395")
    sleep(1)
    poco("com.fdage.eight:id/et_password").set_text("Mo970325")
    sleep(1)
    poco("com.fdage.eight:id/btn_login").click()

    # 测试用例：下载旧场景
    poco("com.fdage.eight:id/iv_scene_cloud").click()
    sleep(3.0)
    poco("com.fdage.eight:id/et_search").click()
    sleep(1.0)
    poco("com.fdage.eight:id/et_search").set_text("xrx")
    sleep(2.0)
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_option", text="下载").click()
    sleep(3.0)
    if poco(text="无法下载，该场景数据未备份").exists():
        logging.info("旧场景无法下载")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(1.0)
    else:
        logging.ERROR("旧场景下载出错")

    # 退出登录
    poco("com.fdage.eight:id/iv_my").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_user_name").click()
    sleep(2.0)
    poco("com.fdage.eight:id/btn_logout").click()
    sleep(1.5)
    poco("com.fdage.eight:id/tv_ok").click()

if __name__ == '__main__':
    pytest.main()
