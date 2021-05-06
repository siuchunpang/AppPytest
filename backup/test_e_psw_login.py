# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_e_psw_login(ini):
    # 连接WiFi
    connect_wifi()

    # 测试用例：错误密码-登录账号
    poco("com.fdage.eight:id/iv_my").click()
    sleep(1.0)
    logging.info("连接wifi")
    poco("com.fdage.eight:id/tv_battery").click()
    sleep(1)
    poco(text=wifi_name).click()
    sleep(1)
    if poco("android:id/button1").exists():
        poco("android:id/button1").click()
    else:
        poco("android:id/button3").click()
    sleep(1)
    poco("向上导航").click()
    sleep(1)

    # 登录
    logging.info("开始登录")
    poco("com.fdage.eight:id/tv_user_name").click()
    sleep(1)
    poco("com.fdage.eight:id/et_phone").set_text("13138102395")
    sleep(1)
    poco("com.fdage.eight:id/et_password").set_text("Aa1234567890")
    sleep(1)
    poco("com.fdage.eight:id/btn_login").click()
    sleep(10)
    if poco("com.fdage.eight:id/tv_login_register", text="密码登录").exists():
        logging.info("输入错误密码,登录失败!")
    else:
        logging.ERROR("ERROR,输入错误密码,登录成功!")


if __name__ == '__main__':
    pytest.main()
