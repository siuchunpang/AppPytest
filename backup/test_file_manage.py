# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_file_manage(ini):
    # 测试用例：检查[文件管理]入口
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

    # 测试用例：文件管理页面布局
    poco("com.fdage.eight:id/tv_file_manage").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_titlebar_title", text="文件管理").wait_for_appearance(10)
    camera = poco("com.fdage.eight:id/tv_cam_id").attr('text')
    storage = poco("com.fdage.eight:id/tv_storage").attr('text')
    logging.info("相机" + camera + "容量：" + storage + "G")
    sleep(2.0)

    # 测试用例：删除文件夹
    poco("com.fdage.eight:id/tv_right", text="选择").click()
    sleep(3.0)
    poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.fdage.eight:id/refreshView").offspring("com.fdage.eight:id/rcv_files").child("android.view.ViewGroup")[
        0].click()
    sleep(1.0)
    poco("com.fdage.eight:id/btn_delete").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_title", text="注意!").wait_for_appearance(5)
    poco("com.fdage.eight:id/tv_ok", text="删除").click()
    sleep(5.0)
    if poco("com.fdage.eight:id/tv_title", text="温馨提示").exists():
        logging.info("文件删除失败")
        poco("com.fdage.eight:id/tv_ok", text="确定").click()
        sleep(1.0)
        poco("com.fdage.eight:id/tv_right", text="取消").click()
        sleep(1.0)
    else:
        logging.info("文件删除成功")
        sleep(5.0)

    # 测试用例：批量删除文件夹
    poco("com.fdage.eight:id/tv_right").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_right").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_left", text="全选").wait_for_appearance(5)
    poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.fdage.eight:id/refreshView").offspring("com.fdage.eight:id/rcv_files").child("android.view.ViewGroup")[
        0].click()
    sleep(3.0)
    poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.fdage.eight:id/refreshView").offspring("com.fdage.eight:id/rcv_files").child("android.view.ViewGroup")[
        1].click()
    sleep(3.0)
    poco("com.fdage.eight:id/btn_delete").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_title", text="注意!").wait_for_appearance(5)
    poco("com.fdage.eight:id/tv_ok", text="删除").click()
    sleep(3.0)
    if poco("com.fdage.eight:id/tv_title", text="温馨提示").exists():
        logging.info("文件批量删除失败")
        poco("com.fdage.eight:id/tv_ok", text="确定").click()
        sleep(1.0)
        poco("com.fdage.eight:id/tv_right", text="取消").click()
        sleep(1.0)
    else:
        logging.info("文件批量删除成功")
    poco("com.fdage.eight:id/iv_left").click()
    sleep(1.0)
    poco("com.fdage.eight:id/iv_my").wait_for_appearance(10)

if __name__ == '__main__':
    pytest.main()