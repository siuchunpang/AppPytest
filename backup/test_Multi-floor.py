# -*- encoding=utf8 -*-
__author__ = "xsl"

import pytest
from tools.tool import *
from tools.config import *
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__, logdir=air_log_path, devices=devices)


def test_addfloor(ini):
    # 新增楼层-拍摄点位
    connect_camera()
    poco("com.fdage.eight:id/iv_menu").wait_for_appearance(5)  # 检查多楼层入口按钮
    shoot()
    poco("com.fdage.eight:id/iv_menu").click()
    sleep(1.0)
    poco("com.fdage.eight:id/iv_add").click()
    sleep(1.0)
    poco(text="新增楼层").wait_for_appearance(5)  # 检查弹框标题
    poco("com.fdage.eight:id/et_input", text="2楼").wait_for_appearance(5)  # 检查新增楼层名称
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(1.0)
    if poco("com.fdage.eight:id/tv_floor", text="2楼").exists():
        logging.info("新增楼层成功")
    else:
        logging.error("新增楼层失败")
    shoot()


def test_editfloor(ini):
    # 修改楼层名称
    poco("com.fdage.eight:id/tv_floor", text="2楼").long_click(2.0)
    sleep(1.0)
    poco("com.fdage.eight:id/iv_edit").click()
    sleep(1.0)
    poco(text="修改楼层名称").wait_for_appearance(5)  # 检查弹框标题
    poco("com.fdage.eight:id/et_input").set_text("")
    poco("com.fdage.eight:id/et_input").set_text("2楼")  # 输入相同楼层名
    sleep(1.0)
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(1.0)
    if poco(text="修改楼层名称").exists():
        logging.info("存在相同楼层名，楼层名称不会修改")
    else:
        logging.error("修改相同楼层名error")
    sleep(1.0)
    poco("com.fdage.eight:id/et_input").set_text("")
    poco("com.fdage.eight:id/et_input").set_text("二楼")
    sleep(1.0)
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(1.0)
    if poco("com.fdage.eight:id/tv_floor", text="二楼").exists():
        logging.info("修改楼层名称成功")
    else:
        logging.error("修改楼层名称失败")


def test_addfloors(ini):
    # 新增2个空楼层
    poco("com.fdage.eight:id/iv_add").click()
    sleep(1.0)
    poco(text="新增楼层").wait_for_appearance(5)
    poco("com.fdage.eight:id/et_input").wait_for_appearance(5)
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(1.0)
    if poco("com.fdage.eight:id/tv_floor").exists():
        logging.info("新增楼层成功")
    else:
        logging.error("新增楼层失败")
    poco("com.fdage.eight:id/iv_add").click()
    sleep(1.0)
    if poco(text="新增失败，已存在空楼层").exists():
        logging.info("已存在空楼层，不会新增楼层")
        poco("com.fdage.eight:id/tv_ok").click()
    else:
        logging.error("新增多个空楼层error")
    sleep(1.0)


def test_switchfloors(ini):
    # 修改点位的楼层
    poco("com.fdage.eight:id/tv_floor", text="二楼").click()
    sleep(1.0)
    poco("com.fdage.eight:id/waveView").long_click(2.0)
    sleep(1.0)
    poco("com.fdage.eight:id/options1").swipe([0.0, 0.079])
    sleep(2.0)
    poco("com.fdage.eight:id/btnSubmit", text="确定").click()
    sleep(2.0)
    poco(text="修改拍摄点").wait_for_appearance(5.0)  # 检查弹框标题
    sleep(1.0)
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(1.0)
    if poco("com.fdage.eight:id/tv_floor", text="二楼").exists():
        logging.error("修改点位楼层error")
    else:
        logging.info("修改点位楼层成功")


def test_deletefloor(ini):
    # 删除楼层
    poco("com.fdage.eight:id/tv_floor", text="3楼").click()
    sleep(1.0)
    poco("com.fdage.eight:id/tv_floor", text="3楼").long_click(2.0)
    sleep(1.0)
    poco("com.fdage.eight:id/iv_delete").click()
    sleep(1.0)
    poco(text="删除楼层").wait_for_appearance(5)  # 检查弹框标题
    poco("com.fdage.eight:id/tv_ok").click()
    sleep(1.0)
    if poco("com.fdage.eight:id/tv_floor", text="3楼").exists():
        logging.error("删除楼层失败")
    else:
        logging.info("删除楼层成功")
    save_scene("Mulitifloor")


if __name__ == '__main__':
    pytest.main(["test_Multi-floor.py"])
