# -*- encoding=utf8 -*-
__author__ = "sjp"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_shoot_check(ini):
    # 测试用例3702，拍照UI排版检查
    connect_camera()
    assert poco("com.fdage.eight:id/iv_left").exists()  # 返回按钮
    assert_equal(poco("com.fdage.eight:id/tv_titlebar_title").get_text(), "拍摄")
    assert_equal(poco("com.fdage.eight:id/tv_right").get_text(), "保存")
    assert poco("com.fdage.eight:id/iv_map_recenter").exists()  # 定位按钮
    assert poco("com.fdage.eight:id/iv_point_operate").exists()  # 点位编辑功能按钮
    assert_equal(poco("com.fdage.eight:id/btn_switch_photo").get_text(), "拍摄")
    assert_equal(poco("com.fdage.eight:id/btn_switch_video").get_text(), "录像")
    assert poco("com.fdage.eight:id/ic_shot").exists()  # 拍摄按钮
    assert poco("com.fdage.eight:id/iv_camset").exists()  # 参数设定按钮


def test_param_check(ini):
    # 测试用例3680，参数设定UI排版检查
    poco("com.fdage.eight:id/iv_camset").click()
    sleep(2)
    assert poco(text="左右拍摄关").exists()  # 左右拍摄按钮
    assert poco(text="定时器").exists()  # 定时器按钮
    assert poco(text="自动模式").exists()  # 自动模式按钮
    assert poco(text="专业模式").exists()  # 专业模式按钮
    assert poco("com.fdage.eight:id/iv_hdr").exists()  # hdr按钮
    poco("com.fdage.eight:id/tv_right").click()
    sleep(2)
    poco("com.fdage.eight:id/iv_left").click()
    sleep(2)


def test_timer_check(ini):
    # 测试用例3713，设置定时器1s/30s/关闭
    connect_camera()
    param(rl=False, timer=-0.26)
    assert_equal(poco("com.fdage.eight:id/tv_timer").get_text(), "1s")
    poco("com.fdage.eight:id/iv_camset").click()
    sleep(2)
    assert poco(text="1s").exists()
    poco("com.fdage.eight:id/tv_right").click()
    sleep(2)
    param(rl=False, timer=0.3)
    assert_equal(poco("com.fdage.eight:id/tv_timer").get_text(), "30s")
    poco("com.fdage.eight:id/iv_camset").click()
    sleep(2)
    assert poco(text="30s").exists()
    poco("com.fdage.eight:id/tv_right").click()
    sleep(2)
    param(rl=False)
    assert not poco("com.fdage.eight:id/tv_timer").exists()
    poco("com.fdage.eight:id/iv_left").click()
    sleep(2)


def test_shoot_rl(ini):
    # 测试用例3707,3704,3460,3703，左右拍摄/自动hdr/左右拍摄中途关闭
    connect_camera()
    param(rl=True, hdr="auto")
    poco("com.fdage.eight:id/ic_shot").click()
    sleep(2)
    poco("com.fdage.eight:id/tv_title", text="请站在相机右侧拍摄(1/2)").wait_for_appearance(120)
    sleep(2)
    poco("com.fdage.eight:id/iv_close").click()
    sleep(2)
    shoot(rl=True)
    save_scene("t_shoot_rl")


def test_shoot_sync(ini):
    # 测试用例3293,3706,3375，同步拍摄/关闭hdr
    connect_camera()
    param(rl=False, hdr="off")
    shoot(rl=False)
    save_scene("t_shoot_sync")


def test_shoot_sync_hdr(ini):
    # 测试用例3376，同步拍摄/开启hdr
    connect_camera()
    param(rl=False, hdr="on")
    shoot(rl=False)
    save_scene("t_shoot_hdr")


if __name__ == '__main__':
    pytest.main(["test_shoot.py"])
