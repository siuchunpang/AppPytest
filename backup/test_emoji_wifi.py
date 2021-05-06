# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_emoji_wifi(ini):
    # 测试用例：连接emoji表情WiFi
    poco("com.fdage.eight:id/iv_my").click()
    sleep(1.0)
    if poco("com.fdage.eight:id/tv_camera_storage", text="未连接").exists():
        logging.info("相机未连接")
        logging.info("连接相机wifi")
        poco("com.fdage.eight:id/tv_battery").click()
        sleep(1.0)
        poco(text=camera_name).click()
        sleep(3.0)
        if poco("android:id/button1").exists():
            poco("android:id/button1").click()
        else:
            poco("android:id/button3").click()
        sleep(10.0)
        poco("向上导航").click()
        sleep(3.0)
    else:
        logging.info("相机已连接")

    poco("com.fdage.eight:id/tv_network").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_wifi_name", text="/xushilin😀").wait_for_appearance(60)
    poco(text="/xushilin😀").click()
    sleep(2.0)
    if poco("com.fdage.eight:id/et_input", text="请输入密码").exists():
        poco("com.fdage.eight:id/et_input").set_text()
        poco("com.fdage.eight:id/et_input").set_text("Aa111111")
        sleep(5.0)
    else:
        sleep(5.0)
    poco("com.fdage.eight:id/tv_network_desc", text="已连接到/xushilin😀").wait_for_appearance(60)
    logging.info("成功连接emoji表情WiFi！")
    poco("com.fdage.eight:id/iv_left")


if __name__ == '__main__':
    pytest.main()