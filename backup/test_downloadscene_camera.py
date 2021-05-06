# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_upload_download(ini):
    # 测试用例3315:同时上传下载场景
    connect_camera()
    param()
    shoot()
    video(120)
    save_scene("t_up-download")
    poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.fdage.eight:id/frag_container").offspring("com.fdage.eight:id/rcv_scene").child(
        "com.fdage.eight:id/root_item")[0].child("com.fdage.eight:id/iv_menu").click()
    sleep(2.0)
    poco("com.fdage.eight:id/tv_option", text="上传").click()
    sleep(2.0)
    poco("com.fdage.eight:id/tv_content", text="相机尚未连接Wi-Fi，点击跳转到连接界面").wait_for_appearance(15)
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(2.0)
    poco(text=wifi_name).wait_for_appearance(60)
    poco(text=wifi_name).click()
    sleep(1.0)
    poco("com.fdage.eight:id/iv_select").wait_for_appearance(60)
    sleep(2.0)
    poco("com.fdage.eight:id/tv_network_desc", text="已连接到%s" % wifi_name).wait_for_appearance(60)
    logging.info("已连接到%s" % wifi_name)
    poco("com.fdage.eight:id/iv_left").click()
    sleep(5.0)
    poco("android.widget.LinearLayout").offspring("android:id/content").offspring(
        "com.fdage.eight:id/frag_container").offspring("com.fdage.eight:id/rcv_scene").child(
        "com.fdage.eight:id/root_item")[0].child("com.fdage.eight:id/iv_menu").click()
    sleep(2.0)
    poco("com.fdage.eight:id/tv_option", text="上传").click()
    sleep(2.0)
    poco("com.fdage.eight:id/tv_ok", text="上传").click()
    sleep(5.0)
    poco("com.fdage.eight:id/iv_scene_cloud").click()
    sleep(8.0)
    poco("com.fdage.eight:id/et_search").set_text("")
    sleep(1.0)
    poco("com.fdage.eight:id/et_search").set_text("AI横琴")
    sleep(2.0)
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(2.0)
    poco(text="下载").click()
    sleep(3.0)
    if poco(text="项目下载中，请到本地查看").exists():
        logging.info("云端项目下载中")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(1.0)
    else:
        logging.ERROR("云端项目下载失败")

    # 测试用例3327：同时下载多个场景
    poco("com.fdage.eight:id/et_search").set_text("")
    sleep(2.0)
    poco("com.fdage.eight:id/et_search").set_text("供应链")
    sleep(2.0)
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(1.0)
    poco(text="下载").click()
    sleep(3.0)
    if poco(text="多个场景无法同时下载，请等待上一个场景下载完后重试").exists():
        logging.info("多个场景无法同时下载")
        poco("com.fdage.eight:id/tv_ok").click()
        sleep(1.0)
    else:
        logging.ERROR("云端项目下载失败")
    poco("com.fdage.eight:id/container_nav_scene_local").click()
    sleep(3.0)
    poco("com.fdage.eight:id/tv_title", text="上传成功").wait_for_appearance(600)
    logging.info("上传成功")
    poco("com.fdage.eight:id/tv_ok", text="确定").click()
    sleep(2)
    poco("com.fdage.eight:id/et_search").click()
    sleep(1.0)
    poco("com.fdage.eight:id/et_search").set_text("AI横琴")
    sleep(2.0)
    poco("com.fdage.eight:id/iv_menu").wait_for_appearance(600)
    logging.info("同时上传下载场景成功")


def test_downloadscene_edit(ini):
    # 测试用例3325:下载场景后，修改场景标题/分类上传
    if poco("com.fdage.eight:id/tv_scene_type", text="其他").exists():
        poco("com.fdage.eight:id/tv_scene_title").click()
        sleep(1.0)
        poco("com.fdage.eight:id/tv_right", text="编辑").click()
        sleep(1.0)
        poco("com.fdage.eight:id/btn_culture_relics", text="文博").click()
        sleep(1.0)
        if poco("com.fdage.eight:id/et_title", text="AI横琴新区人力资源服务产业园").exists():
            poco("com.fdage.eight:id/et_title").set_text("AI横琴新区")
            sleep(1.0)
        else:
            poco("com.fdage.eight:id/et_title").set_text("AI横琴新区人力资源服务产业园")
            sleep(1.0)
    else:
        poco("com.fdage.eight:id/tv_scene_title").click()
        sleep(1.0)
        poco("com.fdage.eight:id/tv_right", text="编辑").click()
        sleep(1.0)
        poco("com.fdage.eight:id/btn_industry_all", text="其他").click()
        sleep(1.0)
        if poco("com.fdage.eight:id/et_title", text="AI横琴新区人力资源服务产业园").exists():
            poco("com.fdage.eight:id/et_title").set_text("AI横琴新区")
            sleep(1.0)
        else:
            poco("com.fdage.eight:id/et_title").set_text("AI横琴新区人力资源服务产业园")
            sleep(1.0)
    sleep(1.0)
    poco("com.fdage.eight:id/tv_right", text="保存").click()
    sleep(2.0)
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_option", text="上传").click()
    sleep(2.0)
    poco(text="点位并未修改，无需上传").wait_for_appearance(15)
    logging.info("P，只修改场景标题分类无法上传场景")
    sleep(1.0)
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(1.0)

    # 删除场景
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_option", text="删除").click()
    sleep(2.0)
    poco("com.fdage.eight:id/tv_ok", text="删除").click()
    sleep(1.0)


if __name__ == '__main__':
    pytest.main(["test_downloadscene_camera.py"])
