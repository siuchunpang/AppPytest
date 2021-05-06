# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


@pytest.mark.run(order=102)
def test_language(ini):
    try:
        poco("com.fdage.eight:id/iv_my").click()
        sleep(1)
        if poco("com.fdage.eight:id/tv_language", text="简体中文").exists():
            logging.info("app当前语言为简体中文")
            poco("com.fdage.eight:id/layout_lan_setting").click()
            sleep(1)
            poco("com.fdage.eight:id/tv_option", text="English").click()
            sleep(3)
            poco("com.fdage.eight:id/tv_language", text="English").wait_for_appearance(10)
            logging.info("lan_setting-EN, success")
            sleep(5)
            poco("com.fdage.eight:id/tv_language", text="English").click()
            sleep(2)
            poco("com.fdage.eight:id/tv_option", text="简体中文").click()
            sleep(3)
            poco("com.fdage.eight:id/tv_language", text="简体中文").wait_for_appearance(10)
            logging.info("lan_setting-CN, success")
        else:
            poco("com.fdage.eight:id/tv_language", text="English").click()
            logging.info("app当前语言为英文")
            poco("com.fdage.eight:id/tv_option", text="简体中文").click()
            sleep(3)
            poco("com.fdage.eight:id/tv_language", text="简体中文").wait_for_appearance(10)
            logging.info("lan_setting-CN, success")
            sleep(5)
            poco("com.fdage.eight:id/layout_lan_setting").click()
            sleep(1)
            poco("com.fdage.eight:id/tv_option", text="English").click()
            sleep(3)
            poco("com.fdage.eight:id/tv_language", text="English").wait_for_appearance(10)
            logging.info("lan_setting-EN, success")

    except Exception as e:
        logging.error("test_language error：" + str(e))
        now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        snapshot(filename=snapShot_path + "\\snapshot_%s.png" % now)


if __name__ == '__main__':
    pytest.main()
