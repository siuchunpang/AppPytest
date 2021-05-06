# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_video_check(ini):
    # 测试用例3338，录像UI排版检查
    connect_camera()
    shoot()
    poco(name="com.fdage.eight:id/btn_switch_video", text="录像").click()
    assert_equal(poco("com.fdage.eight:id/tv_loading").get_text(), "正在加载视频中...")  # 加载视频画面
    sleep(10)
    assert_equal(poco("com.fdage.eight:id/tv_timer").get_text(), "00:00:00")
    assert_equal(poco("com.fdage.eight:id/btn_switch_photo").get_text(), "拍摄")
    assert poco("com.fdage.eight:id/btn_record").exists()  # 录像按钮
    assert poco("com.fdage.eight:id/iv_cam_relocate").exists()  # 定位按钮
    poco("com.fdage.eight:id/btn_switch_photo").click()
    assert_equal(poco("com.fdage.eight:id/tv_loading").get_text(), "正在重置相机设置，请稍等")  # 切换分辨率
    sleep(2)
    poco("com.fdage.eight:id/tv_right").wait_for_appearance(60)
    save_scene("t_video_check")


def test_video_nopoint(ini):
    # 测试用例3693，没有点位点击录像
    connect_camera()
    poco(name="com.fdage.eight:id/btn_switch_video", text="录像").click()
    sleep(2)
    assert_equal(poco("com.fdage.eight:id/tv_content").get_text(), "录制视频需要在至少拍摄一个点后进行")
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(2)
    poco("com.fdage.eight:id/iv_left").click()
    sleep(2)


def test_video(ini):
    connect_camera()
    shoot()
    video(30)
    save_scene("t_video")


if __name__ == '__main__':
    pytest.main()
