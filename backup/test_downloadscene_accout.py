# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_downloadscene_old(ini):
    # 连接WiFi
    connect_wifi()

    # 登录
    logging.info("开始登录")
    poco("com.fdage.eight:id/tv_user_name").click()
    sleep(1.0)
    poco("com.fdage.eight:id/et_phone").set_text("13138102395")
    sleep(1.0)
    poco("com.fdage.eight:id/et_password").set_text("Mo970325")
    sleep(1.0)
    poco("com.fdage.eight:id/btn_login").click()

    # 测试用例3329：下载旧场景
    poco("com.fdage.eight:id/iv_scene_cloud").click()
    sleep(3.0)
    poco("com.fdage.eight:id/et_search").click()
    sleep(1.0)
    poco("com.fdage.eight:id/et_search").set_text("xrx")
    sleep(2.0)
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_option", text="下载").click()
    sleep(3.0)
    if poco(text="无法下载，该场景数据未备份").exists():
        logging.info("旧场景无法下载")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(1.0)
    else:
        logging.ERROR("旧场景下载出错")


def test_downloadscene_new(ini):
    # 测试用例3328：下载新场景
    poco("com.fdage.eight:id/iv_scene_cloud").click()
    sleep(3.0)
    poco("com.fdage.eight:id/et_search").click()
    sleep(1.0)
    poco("com.fdage.eight:id/et_search").set_text("AI横琴")
    sleep(2.0)
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_option", text="下载").click()
    sleep(3.0)
    if poco(text="项目下载中，请到本地查看").exists():
        logging.info("云端项目下载中")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(1.0)
    else:
        logging.ERROR("云端项目下载失败")
    poco("com.fdage.eight:id/container_nav_scene_local").click()
    sleep(3.0)
    poco("com.fdage.eight:id/et_search").click()
    sleep(1.0)
    poco("com.fdage.eight:id/et_search").set_text("AI横琴")
    sleep(2.0)
    poco("com.fdage.eight:id/iv_menu").wait_for_appearance(300)
    logging.info("场景下载成功")
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_option", text="删除").click()
    sleep(2.0)
    poco("com.fdage.eight:id/tv_ok", text="删除").click()
    sleep(1.0)


def test_downloadscene_disconnectwifi(ini):
    # 测试用例3326:下载途中断网再重新下载
    poco("com.fdage.eight:id/iv_scene_cloud").click()
    sleep(3.0)
    poco("com.fdage.eight:id/et_search").click()
    sleep(1.0)
    poco("com.fdage.eight:id/et_search").set_text("AI横琴")
    sleep(2.0)
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_option", text="下载").click()
    sleep(3.0)
    if poco(text="项目下载中，请到本地查看").exists():
        logging.info("云端项目下载中")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(1.0)
    else:
        logging.ERROR("云端项目下载失败")
    poco("com.fdage.eight:id/iv_my").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_battery").click()
    sleep(1.0)
    poco("com.android.settings:id/switch_widget").click()
    sleep(1.0)
    poco("android.widget.ImageButton").click()
    sleep(1.0)
    if poco("下载中断，请在本地点击下载图标重试").exists():
        logging.info("下载途中断网，下载中断")
        sleep(1.0)
        poco("com.fdage.eight:id/tv_ok").click()
    else:
        logging.ERROR("云端项目下载失败")
    poco("com.fdage.eight:id/tv_battery").click()
    sleep(1.0)
    poco("com.android.settings:id/switch_widget").click()
    sleep(5.0)
    poco("android.widget.ImageButton").click()
    sleep(1.0)
    poco("com.fdage.eight:id/container_nav_scene_local").click()
    sleep(3.0)
    poco("com.fdage.eight:id/et_search").click()
    sleep(1.0)
    poco("com.fdage.eight:id/et_search").set_text("AI横琴")
    sleep(2.0)
    poco("com.fdage.eight:id/iv_upload").click()
    sleep(1.0)
    if poco(text="项目下载中，请到本地查看").exists():
        logging.info("云端项目重新下载")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(1.0)
    else:
        logging.ERROR("云端项目下载失败")
    poco("com.fdage.eight:id/iv_menu").wait_for_appearance(300)
    logging.info("场景下载成功")

    # 退出登录
    poco("com.fdage.eight:id/iv_my").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_user_name").click()
    sleep(2.0)
    poco("com.fdage.eight:id/btn_logout").click()
    sleep(1.5)
    poco("com.fdage.eight:id/tv_ok").click()


if __name__ == '__main__':
    pytest.main(["test_downloadscene_accout.py"])
