# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_billingrecords(ini):
    # 连接WIFI
    connect_wifi()

    # 登录
    logging.info("开始登录")
    poco("com.fdage.eight:id/tv_user_name").click()
    sleep(1.0)
    poco("com.fdage.eight:id/et_phone").set_text("13138102395")
    sleep(1.0)
    poco("com.fdage.eight:id/et_password").set_text("Mo970325")
    sleep(1.0)
    poco("com.fdage.eight:id/btn_login").click()
    sleep(3.0)

    # 打开消费记录
    poco("com.fdage.eight:id/tv_expansion_record").click()
    sleep(5.0)

    # 退出登录
    start_app("com.fdage.eight")
    sleep(3.0)
    poco("com.fdage.eight:id/iv_my").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_user_name").click()
    sleep(2.0)
    poco("com.fdage.eight:id/btn_logout").click()
    sleep(1.5)
    poco("com.fdage.eight:id/tv_ok").click()


if __name__ == '__main__':
    pytest.main(["test_billingrecords.py"])
