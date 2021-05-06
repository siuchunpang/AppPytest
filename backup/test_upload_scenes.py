# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_upload_scenes(ini):
    try:
        a = 0
        while a < 3:
            """判断App是否连接相机"""
            poco("com.fdage.eight:id/iv_scene_local").click()
            sleep(1)
            poco("com.fdage.eight:id/floatingBtn").click()
            sleep(2)
            if poco("com.fdage.eight:id/container").exists():
                logging.info("相机已联网")
                poco("com.fdage.eight:id/tv_ok").click()
                sleep(1)
            elif poco("com.fdage.eight:id/disconnect_dialog_ok").exists():
                logging.info("app未连接相机")
                poco("com.fdage.eight:id/disconnect_dialog_ok").click()
                sleep(2)
                if poco("com.android.settings:id/switch_widget").attr('checked') == False:
                    poco("com.android.settings:id/switch_widget").click()
                    sleep(5)
                poco("android:id/title", text=camera_name).click()
                sleep(1.5)
                poco("android:id/button1").click()
                logging.info("正在连接相机...")
                sleep(3)
                poco(name="向上导航").click()
                sleep(10)
                if poco("com.fdage.eight:id/disconnect_dialog_ok").exists() == False:
                    logging.info("app已连接相机")
            else:
                logging.info("相机未联网")

            """拍摄点位"""
            poco(name="com.fdage.eight:id/ic_shot").click()
            sleep(35)
            if poco(name="com.fdage.eight:id/tv_title").exists():
                poco(name="com.fdage.eight:id/ic_shot").click()
                logging.info("左右拍摄开")
                sleep(10)
            else:
                logging.info("左右拍摄关")
            poco(name="android.view.View").wait_for_appearance(timeout=60)

            """录制视频"""
            poco(name="com.fdage.eight:id/btn_switch_video", text="录像").click()
            sleep(5)
            poco("com.fdage.eight:id/iv_cam_relocate").wait_for_appearance(60)
            logging.info("获取视频流画面")
            sleep(5)
            poco(name="com.fdage.eight:id/btn_record").click()
            sleep(30)
            poco(name="com.fdage.eight:id/btn_record").click()
            sleep(30)
            poco("com.fdage.eight:id/bg_btn_playback").wait_for_appearance(120)
            logging.info("录像mp4已保存")
            sleep(2)
            poco(name="com.fdage.eight:id/btn_switch_photo").click()
            sleep(5)
            poco("com.fdage.eight:id/tv_titlebar_title", text="拍摄").wait_for_appearance(30)
            logging.info("返回拍摄界面")
            sleep(5)

            """保存项目"""
            poco(name="com.fdage.eight:id/tv_right", text="保存").click()
            sleep(5)
            poco(name="com.fdage.eight:id/et_title").set_text("")
            sleep(5)
            poco(name="com.fdage.eight:id/et_title").set_text("upload-autotest")
            sleep(5)
            poco(name="com.fdage.eight:id/tv_right").click()
            sleep(5)
            logging.info("保存项目")
            a += 1

        """连接网络"""
        poco(name="com.fdage.eight:id/layout_cam_connection_states").click()
        sleep(8)
        poco(name="com.fdage.eight:id/tv_wifi_name", text="4DAGE-2W-5G").wait_for_appearance(timeout=60)
        poco(name="com.fdage.eight:id/tv_wifi_name", text="4DAGE-2W-5G").click()
        sleep(10)
        poco(name="com.fdage.eight:id/iv_left").click()
        sleep(5)

        """上传场景"""
        poco(name="com.fdage.eight:id/iv_upload")[0].click()
        sleep(1)
        poco(name="com.fdage.eight:id/container").wait_for_appearance(timeout=5)
        poco(name="com.fdage.eight:id/tv_ok", text="上传").click()
        sleep(1)
        poco(name="com.fdage.eight:id/iv_upload")[1].click()
        sleep(1)
        poco(name="com.fdage.eight:id/container").wait_for_appearance(timeout=5)
        poco(name="com.fdage.eight:id/tv_ok", text="上传").click()
        sleep(1)
        poco(name="com.fdage.eight:id/iv_upload")[2].click()
        sleep(1)
        poco(name="com.fdage.eight:id/container").wait_for_appearance(timeout=5)
        poco(name="com.fdage.eight:id/tv_ok", text="上传").click()
        sleep(1)

        b = 0
        while b < 3:
            poco(name="com.fdage.eight:id/tv_title", text="上传成功").wait_for_appearance(timeout=600)
            poco("com.fdage.eight:id/tv_ok", text="确定").click()
            logging.info("上传成功")
            sleep(2.5)
            b += 1

    except Exception as e:
        logging.error("test_upload_scenes error：" + str(e))
        now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
        snapshot(filename=snapShot_path + "\\snapshot_%s.png" % now)


if __name__ == '__main__':
    pytest.main()
