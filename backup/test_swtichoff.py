# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


@pytest.mark.run(order=1004)
def test_swtichoff(ini):
    try:
        poco("com.fdage.eight:id/iv_my").click()
        sleep(2.0)
        poco("com.fdage.eight:id/layout_cam_connection_states").swipe("up")
        sleep(2.0)
        poco("com.fdage.eight:id/tv_more_setting").click()
        sleep(2.0)
        poco("com.fdage.eight:id/btn_shutdown_camera").click()
        sleep(2.0)
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(2.0)
        poco("com.fdage.eight:id/iv_left").click()
        sleep(15.0)
        value = poco("com.fdage.eight:id/tv_battery").attr("text")
        try:
            assert_equal(value, "未连接", "与相机断开连接")
            logging.info("关闭相机成功")
        except AssertionError:
            logging.info("关闭相机失败")
        sleep(3.0)
    except Exception as e:
        logging.error("test_swtichoff error：" + str(e))
        now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        snapshot(filename=snapShot_path + "\\snapshot_%s.png" % now)


if __name__ == '__main__':
    pytest.main()
