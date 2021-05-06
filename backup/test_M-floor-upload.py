# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_add7floor(ini):
    # 新增楼层-拍摄点位
    connect_camera()
    poco("com.fdage.eight:id/iv_menu").wait_for_appearance(5)
    shoot()
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(1.0)

    f = 1
    while f < 7:
        f += 1
        # 拍摄多楼层点位
        poco("com.fdage.eight:id/iv_add").click()
        sleep(1.0)
        poco(text="新增楼层").wait_for_appearance(5)
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(1.0)
        poco("com.fdage.eight:id/tv_floor", text="%s楼" % f).wait_for_appearance(5)
        shoot()

    # 新增楼层-超出7个楼层
    sleep(1.0)
    poco("com.fdage.eight:id/iv_add").click()
    sleep(1.0)
    if poco(text="新增失败，已超出7个楼层").exists():
        logging.info("已超出7个楼层，不会新增楼层")
    else:
        logging.error("新增超出7个楼层error")
    sleep(1.0)
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(1.0)

    # 多楼层场景上传
    save_scene("7floor")
    upload()


if __name__ == '__main__':
    pytest.main(["test_M-floor-upload.py"])
