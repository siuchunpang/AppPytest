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
    #测试用例：版本信息-UI界面检查
    poco("com.fdage.eight:id/iv_my").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_version_info").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_titlebar_title", text="版本信息").wait_for_appearance(10)
    poco("com.fdage.eight:id/iv_logo").wait_for_appearance(10)
    poco("com.fdage.eight:id/tv_app_name", text="四维看看Pro").wait_for_appearance(10)
    poco("com.fdage.eight:id/tv_app_desc").wait_for_appearance(10)
    poco("com.fdage.eight:id/tv_agreement", text="四维看看《用户协议和隐私政策》").wait_for_appearance(10)
    poco("com.fdage.eight:id/tv_copy_right_en", text="Copyright ©2020 4DAGE. All rights reserved.").wait_for_appearance(
        10)
    poco("com.fdage.eight:id/tv_version_name").wait_for_appearance(10)
    version = poco("com.fdage.eight:id/tv_version_name").attr('text')
    logging.info(version)
    sleep(1.0)

    #测试用例：版本信息-版本检查-已是最新版本
    if poco("com.fdage.eight:id/tv_update_notify", text="已是最新版本").exists():
        logging.info("已是最新版本")
    else:
        logging.info("app可更新")

    poco("com.fdage.eight:id/iv_left").click()
    poco("com.fdage.eight:id/iv_my").wait_for_appearance(10)


if __name__ == '__main__':
    pytest.main()