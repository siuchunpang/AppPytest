# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


@pytest.mark.run(order=1001)
def test_fmsd(ini):
    try:
        poco("com.fdage.eight:id/iv_my").click()
        sleep(1.0)
        if poco("com.fdage.eight:id/tv_battery", text="未连接").exists():
            poco("com.fdage.eight:id/tv_battery").click()
            sleep(3.0)
            if poco("com.android.settings:id/switch_widget").attr('checked') == False:
                poco("com.android.settings:id/switch_widget").click()
                sleep(5)
            poco("android:id/title", text=camera_name).click()
            sleep(3)
            poco("android:id/button1").click()
            sleep(3)
            poco(name="向上导航").click()
            sleep(3)
        poco("com.fdage.eight:id/layout_cam_connection_states").swipe("up")
        sleep(2)
        poco("com.fdage.eight:id/tv_more_setting").click()
        sleep(2)
        poco("com.fdage.eight:id/btn_format_sd").click()
        sleep(2)
        poco("com.fdage.eight:id/tv_ok", text="确定").wait_for_appearance(30)
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(2)
        poco("com.fdage.eight:id/tv_content", text="SD卡已格式化").wait_for_appearance(30)
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(2)
        poco("com.fdage.eight:id/iv_left").click()
        value = poco("com.fdage.eight:id/tv_camera_storage").attr("text")
        assert_equal(value, "0.03G/13.66G", "SD卡格式化成功")
    except Exception as e:
        logging.error("test_fmsd error：" + str(e))
        now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        snapshot(filename=snapShot_path + "\\snapshot_%s.png" % now)


if __name__ == '__main__':
    pytest.main()
