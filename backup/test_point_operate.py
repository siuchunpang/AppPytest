# -*- encoding=utf8 -*-
__author__ = "sjp"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_point_operate(ini):
    # 测试用例3345，点位编辑功能UI排版检查
    connect_camera()
    shoot()
    poco("com.fdage.eight:id/iv_point_operate").click()
    sleep(2)
    assert_equal(poco("com.fdage.eight:id/tv_pop_up_content").get_text(), "1.闪烁为选中的拍摄点，轻按可切换拍摄点\n2.长按拍摄点可进行删除操作")


def test_point_delete(ini):
    # 测试用例3351,3352，取消删除点位和删除照片点位
    poco("com.fdage.eight:id/waveView").long_click()
    sleep(2)
    assert_equal(poco("com.fdage.eight:id/tv_content").get_text(), "删除最后一个点位后，所有场景数据将会清空，是否删除？")
    poco("com.fdage.eight:id/tv_cancel").click()
    sleep(2)
    poco("com.fdage.eight:id/waveView").long_click()
    sleep(2)
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(2)


def test_point_delete1(ini):
    # 测试用例3350，删除视频点位
    shoot()
    video(5)
    poco("com.fdage.eight:id/iv_point_operate").click()
    sleep(2)
    poco("com.fdage.eight:id/waveView").long_click()
    sleep(2)
    poco("com.fdage.eight:id/btn_cancel").click()
    sleep(2)
    poco("com.fdage.eight:id/waveView").long_click()
    sleep(2)
    poco(text="删除整个拍摄点").click()
    sleep(2)
    assert_equal(poco("com.fdage.eight:id/tv_content").get_text(), "删除最后一个点位后，所有场景数据将会清空，是否删除？")
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(2)
    shoot()
    video(5)
    poco("com.fdage.eight:id/iv_point_operate").click()
    sleep(2)
    poco("com.fdage.eight:id/waveView").long_click()
    sleep(2)
    poco(text="仅删除拍摄点的视频").click()
    sleep(2)
    assert_equal(poco("com.fdage.eight:id/tv_content").get_text(), "即将删除第1个点视频数据\n确认删除")
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(2)
    poco("com.fdage.eight:id/iv_point_operate").click()
    sleep(2)
    save_scene("t_point_delete1")


def test_point_delete2(ini):
    result = "T"
    # 测试用例3351,3352，删除第二个点位
    connect_camera()
    shoot()
    if shoot():
        poco("com.fdage.eight:id/iv_point_operate").click()
        sleep(2)
        poco("com.fdage.eight:id/waveView").long_click()
        sleep(2)
        assert_equal(poco("com.fdage.eight:id/tv_content").get_text(), "删除第2个点\n删除后拍摄点会重新排序")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(2)
        poco("com.fdage.eight:id/iv_point_operate").click()
        sleep(2)
    else:
        result = "F"
    save_scene("t_delete_point" + result)


'''
def test_point_swipe(ini):
    result = "T"
    # 测试用例3427，拖动点位
    connect_camera()
    shoot()
    if shoot():
        poco("com.fdage.eight:id/iv_point_operate").click()
        sleep(2)
        assert_equal(poco("com.fdage.eight:id/tv_pop_up_content").get_text(),
                     "1.闪烁为选中的拍摄点，轻按可切换拍摄点\n2.长按拍摄点可进行删除操作\n3.仅最后的拍摄点可移动调整")
        poco("com.fdage.eight:id/iv_point_box").swipe("up")
        sleep(2)
        assert poco("com.fdage.eight:id/btn_cancel").exists()
        assert poco("com.fdage.eight:id/btn_confirm").exists()
        poco("com.fdage.eight:id/btn_confirm").click()
        sleep(2)
        poco("com.fdage.eight:id/tv_title").wait_for_disappearance()
        poco("com.fdage.eight:id/iv_point_operate").click()
        sleep(2)
    else:
        result = "F"
    save_scene("t_swipe_point" + result)
'''

if __name__ == '__main__':
    pytest.main()
