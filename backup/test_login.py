# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


@pytest.mark.run(order=101)
def test_login(ini):
    # 连接wifi
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
    if poco("com.fdage.eight:id/tv_user_name").attr("text") == "xushilin":
        logging.info("登录成功")
    else:
        logging.info("登录失败")

    # 退出登录
    poco("com.fdage.eight:id/tv_user_name").click()
    sleep(1)
    poco("com.fdage.eight:id/btn_logout").click()
    sleep(1)
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(1)
    logging.info("确定退出登录")
    if poco("com.fdage.eight:id/tv_user_name").attr("text") == "登录/注册":
        logging.info("退出登录成功")
    else:
        logging.info("退出登录失败")


if __name__ == '__main__':
    pytest.main(["test_login.py"])
